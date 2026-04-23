from pathlib import Path
# LangChain deprecated - đã migrate sang langchain-core
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

OLLAMA_BASE_URL = "http://localhost:11434"
LLAMA_MODEL = "llama3.1:latest"
PERSIST_DIR = "chroma_db"


def load_documents(source_path: Path):
    # Dùng glob thay vì os.walk vì cần filter extension trước khi đọc
    # Giảm số lần gọi hệ thống, nhất là khi có nhiều file không cần thiết
    docs = []
    if source_path.is_dir():
        for path in source_path.glob("**/*"):
            if path.is_file() and path.suffix.lower() in {".txt", ".md"}:
                docs.append(TextLoader(str(path), encoding="utf-8").load()[0])
    elif source_path.is_file():
        docs.append(TextLoader(str(source_path), encoding="utf-8").load()[0])
    return docs


def build_vector_store(documents):
    # chunk_overlap=200 để đảm bảo context liên tục giữa các chunk
    # Nếu overlap quá nhỏ, thông tin ở ranh giới có thể bị mất
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = []
    for doc in documents:
        docs.extend(text_splitter.split_documents([doc]))

    embeddings = OllamaEmbeddings(
        model=LLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
    )

    return Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )


def build_qa_chain(retriever):
    # temperature=0.0 để đảm bảo output nhất quán, phù hợp cho RAG
    # Không cần creativity trong việc trả lời dựa trên context
    llm = Ollama(
        model=LLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.0,
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )


def main():
    data_path = Path("summary")
    # Tạo thư mục nếu chưa có - tránh lỗi khi chạy lần đầu
    data_path.mkdir(exist_ok=True)

    docs = load_documents(data_path)
    if not docs:
        print("Không tìm thấy tài liệu trong thư mục `summary`. Vui lòng thêm file .txt hoặc .md.")
        return

    vector_store = build_vector_store(docs)
    vector_store.persist()

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    qa = build_qa_chain(retriever)

    print("Native RAG với Ollama llama3.1 đã sẵn sàng.")
    while True:
        query = input("\nNhập câu hỏi (hoặc gõ 'exit' để thoát): ").strip()
        if not query or query.lower() == "exit":
            break

        result = qa.run(query)
        print("\n=== Kết quả ===")
        print(result)


if __name__ == "__main__":
    main()
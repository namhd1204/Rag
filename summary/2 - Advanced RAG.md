Trong bối cảnh rộng hơn của các mô hình RAG chính, **Advanced RAG (RAG nâng cao)** được các nguồn tài liệu xác định là bước tiến hóa thứ hai, ra đời nhằm mục tiêu cụ thể là khắc phục những thiếu sót của mô hình Naive RAG truyền thống.

Dưới đây là các thông tin chi tiết về Advanced RAG dựa trên các nguồn:

### 1. Mục tiêu và Cấu trúc cốt lõi
Advanced RAG không thay đổi bản chất của quy trình "Truy xuất - Đọc" mà tập trung vào việc **tinh chỉnh chất lượng thông tin** thông qua các bước bổ sung.
*   **Vượt qua hạn chế của Naive RAG:** Advanced RAG giải quyết các vấn đề như độ chính xác truy xuất thấp (lấy nhầm nhiễu), khả năng thu hồi thấp (bỏ lỡ thông tin quan trọng) và sự thiếu gắn kết trong văn bản tạo ra.
*   **Bổ sung hai quy trình then chốt:** Khác với quy trình tuyến tính đơn giản, Advanced RAG tích hợp thêm các giai đoạn **Tiền truy xuất (Pre-retrieval)** và **Hậu truy xuất (Post-retrieval)**.

### 2. Các kỹ thuật tối ưu hóa đặc trưng
Các nguồn tài liệu mô tả chi tiết nhiều kỹ thuật nâng cao được áp dụng trong mô hình này:
*   **Tối ưu hóa lập chỉ mục (Indexing):** Sử dụng chiến lược cửa sổ trượt (sliding window), phân đoạn dữ liệu tinh vi (fine-grained segmentation) và bổ sung metadata để tăng khả năng lọc dữ liệu. Việc sử dụng **Chỉ mục đồ thị (Graph Indexing)** cũng giúp cải thiện đáng kể độ chính xác cho các câu hỏi đòi hỏi suy luận nhiều bước.
*   **Tối ưu hóa Tiền truy xuất:** Bao gồm việc **mở rộng truy vấn (Query Expansion)**, viết lại truy vấn (Query Rewrite) hoặc bình thường hóa câu hỏi để căn chỉnh tốt hơn với cơ sở dữ liệu. Kỹ thuật **HyDE** thậm chí tạo ra một tài liệu giả thuyết để tìm kiếm các tài liệu thực sự có sự tương đồng về ngữ nghĩa cao hơn.
*   **Tối ưu hóa Hậu truy xuất:** Sau khi lấy được dữ liệu, hệ thống sẽ thực hiện **Xếp hạng lại (ReRank)** để đưa các thông tin phù hợp nhất lên đầu và **Nén Prompt (Prompt Compression)** để loại bỏ nhiễu, giúp LLM tập trung vào nội dung quan trọng mà không vượt quá giới hạn ngữ cảnh.

### 3. Các biến thể và phương pháp tiếp cận mới
Nhiều nghiên cứu trong các nguồn đã đề xuất các mô hình Advanced RAG chuyên biệt:
*   **Focus Mode:** Thay vì truy xuất toàn bộ tài liệu, kỹ thuật này chỉ trích xuất những câu thiết yếu nhất, giúp cân bằng giữa độ phong phú ngữ cảnh và hiệu quả truy xuất.
*   **Stimulus RAG (SRAG):** Một phương pháp mới sử dụng "gợi ý" (hint) được trích xuất từ các tài liệu hàng đầu để kích thích LLM tạo ra câu trả lời chính xác hơn, vượt qua cả hiệu suất của việc tinh chỉnh mô hình (fine-tuning).
*   **RAG Đa phương thức (Multimodal RAG):** Mở rộng Advanced RAG sang lĩnh vực kiến trúc và kỹ thuật bằng cách xử lý đồng thời văn bản, hình ảnh sơ đồ và bảng biểu phức tạp thông qua không gian nhúng chung.

### 4. Vị trí trong lộ trình phát triển
Trong sơ đồ tiến hóa, Advanced RAG nằm giữa Naive RAG và **Modular RAG**.
*   Trong khi Advanced RAG tập trung vào việc làm mượt và tối ưu hóa các bước trong quy trình sẵn có, Modular RAG sẽ tiến xa hơn bằng cách phá vỡ cấu trúc tuyến tính để cho phép các mô-đun (như tìm kiếm, bộ nhớ, kiểm chứng) được sắp xếp linh hoạt tùy theo bài toán.

Tóm lại, Advanced RAG đóng vai trò là giải pháp **tối ưu hóa quy trình chuyên sâu**, sử dụng các kỹ thuật tinh vi để đảm bảo rằng LLM nhận được thông tin chính xác, liên quan và sạch sẽ nhất có thể trước khi thực hiện nhiệm vụ sinh văn bản.
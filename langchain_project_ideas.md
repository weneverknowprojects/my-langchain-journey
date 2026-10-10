# LangChain Project Ideas from Easy to Hard

## Fase 1: Easy (Fundamental & RAG Dasar)
Dua project ini dirancang untuk membangun insting dasar terhadap core components LangChain sebelum masuk ke arsitektur agentik yang kompleks.

### 1.1 Structured Data Generator (Marketing Copy & Product JSON)
Membangun pipeline AI sederhana yang menerima input berupa nama produk atau fitur mentah, lalu menghasilkan deskripsi marketing, struktur harga, dan launcher text dalam format JSON yang terstruktur dan valid.

Yang akan dipelajari:

LLM & Chat Models: Cara inisialisasi dan memanggil model (seperti OpenAI, Anthropic, atau OpenRouter LLMs).

Prompt Templates: Mengelola instruksi dinamis dengan variabel input tanpa menggunakan f-strings standar.

Output Parsers: Menggunakan PydanticOutputParser atau StructuredOutputParser untuk memaksa LLM mengembalikan format JSON yang bisa langsung dikonsumsi oleh backend/API.

LCEL (LangChain Expression Language): Menulis chain modern menggunakan sintaks pipe (prompt | model | parser).

### 1.2 Basic Document Q&A (RAG Bot untuk PRD/SOP)
Membangun bot berbasis terminal atau web sederhana yang membaca dokumen teks atau PDF (misalnya dokumen spesifikasi produk atau SOP operasional), lalu mengizinkan pengguna untuk menanyakan informasi spesifik yang ada di dalam dokumen tersebut.

Yang akan dipelajari:

Document Loaders: Mengimpor data dari file PDF, teks, atau Markdown ke dalam ekosistem LangChain.

Text Splitters: Memecah dokumen panjang menjadi chunk kecil agar muat di dalam konteks token LLM (menggunakan RecursiveCharacterTextSplitter).

Embeddings & Vector Stores: Mengubah teks menjadi vektor ruang dan menyimpannya di vector database lokal (seperti Chroma atau FAISS).

Retrieval Chains: Menghubungkan retriever dengan LLM untuk menghasilkan jawaban yang secara ketat didasarkan pada dokumen sumber.

## Fase 2: Intermediate (Tool Calling, Memory & Routing)
Project di fase ini mulai memperkenalkan otonomi dan pengelolaan state, komponen kunci untuk membangun sistem multi-tenant atau bot gateway.

### 2.1 Telegram Gateway Bot dengan Semantic Routing
Membangun bot Telegram yang memiliki percakapan persisten dan mampu melakukan routing pertanyaan secara cerdas. Jika pengguna bertanya tentang kasual, bot menggunakan chain obrolan biasa. Jika pengguna mengirimkan URL, bot menggunakan chain summarization untuk membaca halaman tersebut.

Yang akan dipelajari:

Memory Management: Menyimpan dan mengambil riwayat percakapan menggunakan ConversationBufferMemory atau penyimpanan memori berbasis database (SQLite/Redis) via LangChain.

Semantic Routing / RunnableBranch: Membuat logika percabangan di dalam LCEL, di mana LLM memutuskan chain mana yang harus dieksekusi berdasarkan klasifikasi intent pengguna.

Web Loaders: Menggunakan WebBaseLoader untuk scraping teks dari URL secara langsung.

### 2.2 Database & API Agent untuk Operasional Retail
Membuat agent yang tidak hanya menjawab teks, tetapi dapat mengambil tindakan. Agent ini dihubungkan dengan database lokal (contoh: SQLite berisi data inventory/POS) dan tool kalkulator. Pengguna bisa bertanya "Berapa total stok barang X dan kalikan dengan harganya."

Yang akan dipelajari:

Agents & ReAct Framework: Memahami paradigma Reasoning and Acting, di mana LLM merencanakan langkah sebelum mengeksekusinya.

Tool Calling: Membuat dan mendaftarkan custom tools (fungsi Python/API calls) yang bisa dipicu oleh LLM secara mandiri.

SQLDatabaseChain / SQL Toolkit: Cara aman memberikan LLM akses untuk melakukan query read-only ke dalam skema database relasional.

## Fase 3: Advanced (Multi-Agent Orchestration & Stateful Workflows)
Fase ini menggunakan LangGraph (ekstensi LangChain untuk stateful, multi-actor applications) untuk mensimulasikan alur kerja engineering yang nyata.

### 3.1 Desktop AI Assistant untuk Software Engineering Workflow
Membangun asisten lokal (CLI/API) dengan arsitektur multi-agent berbasis supervisor. Terdapat satu "Supervisor Agent" yang menerima perintah pengguna (misal: "Analisis repository lokal ini dan buatkan list bug potensial"), lalu mendelegasikan tugas ke dua worker agents:

Code Reader Agent: Bertugas membaca struktur direktori dan isi file kode lokal menggunakan custom tools (mirip arsitektur MCP).

Reviewer Agent: Menerima kode yang dibaca, menganalisis logic/API, dan memberikan rekomendasi perbaikan.
Supervisor kemudian menggabungkan hasil kerja mereka menjadi satu output akhir.

Yang akan dipelajari:

LangGraph Fundamentals: Mengganti chain linear (LCEL) dengan graphs (StateGraph) yang memiliki nodes (agents/tools) dan edges (conditional routing).

Multi-Agent Delegation: Membangun hierarki agent, di mana agent dapat saling berkomunikasi dan mengoper state atau hasil eksekusi satu sama lain.

Cyclic Workflows: Membuat loop eksekusi (contoh: agent akan terus mencoba memperbaiki error pemanggilan API sampai berhasil atau mencapai batas iterasi).

Local Execution & Custom Environment: Menyatukan eksekusi skrip lokal, pembacaan repository, dan LLM routing dalam satu sandbox eksekusi yang kohesif.
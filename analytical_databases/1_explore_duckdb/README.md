# DuckDB
DuckDB is an in process analytical database management system. The goal of DuckDB is to enable analysis of data using standard SQL queries without the overhead of copying the data to an external system or requiring a specialized query interface. DuckDB is currently in development and close to its 1.x release.

## In memory / out of memory
DuckDB is an in-memory database. This means that all data is stored in memory and that no data is written to disk. This is in contrast to traditional database systems that write data to disk. The advantage of in-memory databases is that they are much faster than traditional databases. Still DuckDB can use disk to swap out data during query execution. This allows DuckDB to handle datasets that are larger than the available memory. The performance hit for out-of-memory execution is not that big if the disk is a modern solid state disk.

## Arrow
DuckDB supports the Arrow format for columnar data. Arrow is a cross-language development platform for in-memory data. It specifies a standardized language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations on modern hardware. It also provides computational libraries and zero-copy streaming messaging and interprocess communication. Languages currently supported include C, C++, C#, Go, Java, JavaScript, MATLAB, Python, R, Ruby, and Rust.

## Goal
Here we will look at different data sources and how to manage these DuckDB. We will use the SQL and Spark APIs to perform our queries and analytics. 
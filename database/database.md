### Databases Notes

![0_kUHyd26FyzKeoiZX](https://github.com/user-attachments/assets/160c0a6d-e9ec-4da7-9de3-ee8f7134b736)

![0_lbtSAeYRtmUMAWeY](https://github.com/user-attachments/assets/d80ef9ed-dcf6-47f4-be02-3f5f9fdce78f)

#### 1. **Fundamentals of Databases**
   - **Types of Databases**: Relational (SQL), Non-relational (NoSQL)
   - **Database Management Systems (DBMS)**: Software for creating and managing databases (e.g., MySQL, PostgreSQL, MongoDB, DynamoDB)
   - **Data Models**: Schemas, tables, relationships for SQL; collections, documents for NoSQL
   - **CRUD Operations**: Create, Read, Update, Delete

#### 2. **Relational Databases (SQL)** 
   ![rdbms](https://github.com/user-attachments/assets/f374d8a6-328e-44ef-8edb-3527cb9667a9)

   - SQL stand for structured query language which is used for update, delet, insert data in table or Relational database.
   - **SQL Basics**: SELECT, INSERT, UPDATE, DELETE
   - **Joins**: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN
   - **Indexes**: Improve query performance, types (B-Tree, Hash)
   - **Transactions**: ACID properties (Atomicity, Consistency, Isolation, Durability)
   - **Normalization**: Organizing data to reduce redundancy (1NF, 2NF, 3NF)

#### 3. **Non-relational Databases(NoSQL)**
   - **Types of NoSQL Databases**: Document-based (e.g., MongoDB), Key-Value (e.g., Redis), Column-family (e.g., Cassandra), Graph (e.g., Neo4j)
   - **Basic Operations**: Inserting, querying, updating documents or key-value pairs
   - **Use Cases**: Scalability, unstructured data, flexibility in schema design

#### 4. **AWS Database Services**
   - **Amazon RDS**: Managed relational database service (supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server)
     - **Key Features**: Automated backups, Multi-AZ deployments, Read replicas
   - **Amazon DynamoDB**: Managed NoSQL database service
     - **Key Features**: Single-digit millisecond response time, Auto-scaling, Global tables
   - **Amazon Aurora**: High-performance, MySQL- and PostgreSQL-compatible relational database
     - **Key Features**: Serverless option, Global database, Fault-tolerant
   - **Amazon Redshift**: Data warehousing service
     - **Key Features**: Columnar storage, Massively parallel processing (MPP), Integration with BI tools
   - **Amazon ElastiCache**: In-memory caching service (supports Redis, Memcached)
     - **Key Features**: Low latency, High throughput, Redis replication, and clustering

#### 5. **Database Security**
   - **Encryption**: Data at rest and in transit
   - **IAM Policies**: Granting and restricting access
   - **VPC**: Using VPCs and subnets to secure database access
   - **Backups and Recovery**: Automated backups, snapshots, point-in-time recovery

#### 6. **Monitoring and Performance Tuning**
   - **AWS CloudWatch**: Monitoring database metrics and setting alarms
   - **Performance Insights**: Analyzing and optimizing database performance
   - **Database Tuning**: Query optimization, indexing strategies, read/write partitioning

#### 7. **Backup and Recovery**
   - **Automated Backups**: Configuring backup retention, scheduling
   - **Snapshots**: Manual and automated snapshots
   - **Restoration**: Restoring from snapshots and backups

#### 8. **Migration**
   - **AWS Database Migration Service (DMS)**: Migrating databases to AWS
     - **Key Features**: Minimal downtime, Schema conversion tool
   - **Strategies**: Homogeneous (same DB engine), Heterogeneous (different DB engines)

#### Simplest Learning Notes
- **CRUD Operations**: Basic building blocks of database interaction
- **Indexes and Joins**: Essential for performance and complex queries
- **ACID Transactions**: Critical for data integrity in relational databases
      ACID compliance refers to a set of properties that ensure reliable processing of database transactions. These properties are:

      1. **Atomicity**: Ensures that all parts of a transaction are completed successfully. If any part of the transaction fails, the entire transaction is rolled back, and no changes are applied.
      2. **Consistency**: Ensures that a transaction brings the database from one valid state to another, maintaining the integrity of the data.
      3. **Isolation**: Ensures that the intermediate state of a transaction is invisible to other transactions, preventing concurrent transactions from affecting each other.
      4. **Durability**: Ensures that once a transaction is committed, it remains in the system even in the event of a system failure.

ACID compliance is crucial for applications requiring high reliability and consistency, such as financial transactions and critical data processing systems. 
- **Normalization**: Reduces redundancy, ensures data integrity
- **RDS vs. DynamoDB**: RDS for structured, relational data; DynamoDB for flexible, scalable NoSQL
- **Security Best Practices**: Encrypt data, restrict access with IAM, use VPCs
- **Performance Monitoring**: Use CloudWatch, Performance Insights to identify bottlenecks
- **Backup and Recovery**: Regular backups, snapshots, know how to restore
- **Migration Tools**: AWS DMS for seamless migration

Focusing on these core concepts will provide a solid foundation in database management and operations as an AWS DevOps engineer.

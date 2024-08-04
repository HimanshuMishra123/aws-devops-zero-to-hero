### Databases Notes

![0_kUHyd26FyzKeoiZX](https://github.com/user-attachments/assets/160c0a6d-e9ec-4da7-9de3-ee8f7134b736)
---
![0_lbtSAeYRtmUMAWeY](https://github.com/user-attachments/assets/d80ef9ed-dcf6-47f4-be02-3f5f9fdce78f)
---
![A](https://github.com/user-attachments/assets/10d6e087-22de-4cd0-9e3a-5eb748760920)
---
![DBBLOG-1382-1-WHITE](https://github.com/user-attachments/assets/3a6f4718-6978-4431-9e44-31115d8150ce)
---

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
   - **Examples**: MySQL, PostgreSQL, Oracle, SQL Server.

#### 3. **Non-relational Databases(NoSQL)**
   - **Types of NoSQL Databases**: Document-based (e.g., MongoDB), Key-Value (e.g., Redis), Column-family (e.g., Cassandra), Graph (e.g., Neo4j)
   - **Basic Operations**: Inserting, querying, updating documents or key-value pairs
   - **Use Cases**: Scalability, unstructured data, flexibility in schema design

#### Use Cases:
- **SQL**: Ideal for applications requiring complex queries, transactions, and relationships between data, such as financial systems, ERP systems, and traditional web applications.
- **NoSQL**: Suitable for applications with large volumes of unstructured data, requiring high scalability and flexibility, such as real-time analytics, content management systems, and big data applications.

#### 4. **AWS Database Services** (Refer Excel file name Database-comparison.xlsx for better understanding)
![Book1](https://github.com/user-attachments/assets/53dcb329-2a83-4bd4-bebd-804fd5a1bc52)
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

      - Mostly all SQL databases are designed to be ACID compliant, whereas NoSQL is a vast ecosystem of entirely different architectures and servers. Many of them are, in fact by design, not ACID compliant. Many will sacrifice reliability for speed.(But Amazon Dynamodb and Amazon Neptune provide Built-in support for ACID transactions).
      
      - ACID compliance is crucial for applications requiring high reliability and consistency, such as financial transactions and critical data processing systems. 

- **Normalization**: Reduces redundancy(eliminate repetition), ensures data integrity
      **Explain the concept of database normalization. Why is it important, and what are some common normal forms used in relational databases?**

      **Normalization**:
      - **Definition**: Database normalization is the process of organizing a database to reduce redundancy and improve data integrity. It involves decomposing tables into smaller, related tables and defining relationships between them.

      **Importance**:
      - **Reduces Redundancy**: By eliminating duplicate data, normalization helps save storage space and reduces the risk of inconsistencies.
      - **Improves Integrity**: Ensures that data dependencies are correctly enforced, reducing anomalies and ensuring data accuracy.

      **Common Normal Forms**:(not that much important)
      - **First Normal Form (1NF)**: Requires that each column contain atomic (indivisible) values and that each column in a table has a unique name.
      - **Second Normal Form (2NF)**: Achieved when a table is in 1NF and all non-key attributes are fully functionally dependent on the entire primary key (not just part of it).
      - **Third Normal Form (3NF)**: Achieved when a table is in 2NF and all the attributes are functionally dependent only on the primary key, not on other non-key attributes (eliminating transitive dependency).

- **RDS vs. DynamoDB**: RDS for structured, relational data; DynamoDB for flexible, scalable NoSQL
- **Security Best Practices**: Encrypt data, restrict access with IAM, use VPCs
- **Performance Monitoring**: Use CloudWatch, Performance Insights to identify bottlenecks
- **Backup and Recovery**: Regular backups, snapshots, know how to restore
- **Migration Tools**: AWS DMS for seamless migration


**How do you handle database backups and recovery in a production environment? Can you discuss any tools or strategies you use to ensure data integrity and minimize downtime?**

   **Backups**:
   - **Types**: Perform regular full backups (complete snapshot of the database) and incremental or differential backups (only the changes since the last backup) to ensure data can be restored with minimal loss.
   - **Scheduling**: Implement a backup schedule that balances the need for up-to-date backups with resource usage. This might include daily full backups and more frequent incremental backups.
   - **Testing**: Regularly test backups to ensure they can be restored successfully and verify the integrity of the backed-up data.

   **Recovery**:
   - **Tools**: Use built-in database tools for backup and recovery, such as `mysqldump` for MySQL, `pg_dump` for PostgreSQL, or specialized tools like AWS RDS automated backups for managed services.
   - **Disaster Recovery Plan**: Develop a comprehensive disaster recovery plan that includes steps for data restoration, application recovery, and failover procedures.
   - **High Availability**: Implement high availability solutions like database clustering, replication, and failover mechanisms to minimize downtime and ensure continuous access to data.

   **Strategies**:
   - **Automate**: Use automation tools to schedule and manage backups, reducing manual intervention and the risk of human error.
   - **Monitor**: Continuously monitor backup processes and storage to ensure backups are completed successfully and there are no issues with the backup systems.

### Website scenario with API engine and Database Management System in an on-premises data center
![website-scenario-with-api-engine](https://github.com/user-attachments/assets/375261b5-8bb6-4cba-ab52-6c88906a9efc)
https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/website-scenario-with-api-engine-and-database-management-system-in-an-on-premises-data-center.html

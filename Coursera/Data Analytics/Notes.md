# Types of Data

- Structured data: well organized, can be stored in databases and lends itself to standard data analysis methods and tools
    - SQL Databases
    - Online Transaction Prcoessing
    - Spreadsheets
    - Online forms
    - Sensors (GPS, RFID)
    - Server logs
- Unstructured data: semi-structured, somewhat organized, relies on meta tags for grouping and hierarchy
    - Emails
    - XML and other markup languages
    - Binary executables
    - TCP/IP packets
    - Zipped files
    - Integration of data
- Unstructured data - not conventionally organized (jpegs, web pages)

## File Types and Formats

Delimited text files
- files used to store data as text
- each value is separated by a delimiter (comma, in CSV)
- others include tab, colon, vertical bar, space
- TSV is common if the data contains commas

XLSX
- spreadsheet
- XML file format
- open file format - accessible to other applications (and functions too)
- pretty secure, can't contain malicious code

XML
- readable by both humans and machines
- does not use predefined tags

PDF

JSON
- key:value pairs
- can be used in any language
- really useful

# Sources of Data

Relational Databases
- store structured data

Flat File and XML Datasets
- store in plain text, one record per line
- maps to a single table (unlike RDB)
- spreadsheets are special - can contain multiple worksheets
- XML - contain data values that are ID's or marked-up using tags
    - can support complex data structures

APIs and Web Services
- web scraping can extract data from unstructured sources

Data Streams and Feeds
- aggregation streams of data flowing from instruments, IOT devices, GPS data, applications/programs, websites, social media feeds
- RSS - really simple syndication
    - capturing updated data from online forums

# Languages for Data Professionals

Query
- SQL - used mostly for Relational DBs
Programming
- Python
- R
- Java
Shell
- Bash
- PowerShell

# Data Repositories and Big Data Stores

NoSQL is widely used for processing big data, which is often stored in data warehouses
- Data warehouses work as a central repository that merges information coming from disparate sources and consolidates it through the ETL process into one comprehensive database for analytics and BI
- At a very high level, ETL helps you extract data from different sources, transform it into a clean and usable state, and load the data into the enterprise's data repository
- Overall, repositories help to isolate data and make reporting and analytics more efficient and credible

## RDMS

Relational databaes build on the organizational principles of flat flies such as spreadsheets, with data organized into rows and columns following a well-defined schema - but this is where the similarities end
- RDBs are ideal for large volumes
- each table has a unique set of rows and columns
- relationships can be defined b/w tables
- fields can be restricted to specific data types and values
- security architectures of a RDB is more secure - greater access control and governance

Advantages
- create meaningful information by joining tables
- flexibility to make changes while db in use
- minimize data redundancy by allowing relationships b/w tables
- ease of backup and DR
- ACID compliant (Atomicity, Consistency, Isolation, Durability)

Use Cases
- OLTP (Online Transaction Processing)
- Data Warehouses (Online analytical processes, OLAP)

Limitations
- only works well with structure
- migration is difficult
- fixed lengths for data fields

## NoSQL

Built for specific models and have flexible schemas
- allows data to be stored in a sem

Types
- Key:Value store
    - great for user sessions
    - not great if you want to query data on a specific value (since you need the key), need relationships b/w values, and need multiple unique keys
- Document-based
    - store each record and its assocated data within a single document
    - enables flexible indexing, powerful ad hoc queries, and analytics of collections of documents
    - preferred for eCommerce, medical records, CRM, analytics platforms
    - not great for complex queries
- Column-based
    - data is stored in cells groups as columns of data instead of rows
    - a logical grouping of columns is called a column family
    - great for time-series, weather, etc
    - not great for complex queries and if you change querying patterns frequently
- Graph
    - good for working with interconnnected data
    - social networks, access management
    - not greate for high volumes

Advantages of NoSQL
- can handle large volumes of structured, semi-structured, and unstructured data
- can run distributed across many datacenters
- efficient and cost effective
- simpler design, better control over availability, improved scalability make it agile, flexible, and support quick iterations

## Data Marts, Lakes, and Pipelines

Data warehouse - by the time it comes in, it's analysis ready
- data has been modeled and structured for a specific purpose
- you would use this if you have lots of data from multipe systems

Data mart - subsection of the data warehouse
- provide data relevant to those that need it
- gives isolated security and performance
- business-specific reporting and analytics

Data Lake - data in raw formats
- pool of raw data where each element is given a unique identifier and tagged with meta-tags for further use
- sometimes used as a staging area

Data Pipelines
- ETL
- Gather raw data
- Extract information for your needs
- Clean, standardize, transform
- Load into a repository

Extract
- source data is moved from source system to staging area
- can be batch or stream

Transform
- standardizing, removing duplicate
- filtering out data not required
- enriching data (splitting name into first, last)
- establishing key relationships across table
    - applying business rules and data validations

Load - processed data is moved to destination system
- initial - all of it
- incremental - as needed
- full-refresh - erasing, reloading with fresh data
- load verification
    - checks for missing or null values, server performance, load failures

Pipeline is a broader term of moving data from one system to another, ETL is just a subset


## Foundations of Big Data

Common elements
- Velocity - speed at which data accumulates
    - very fast
- Volume - scale of the data
    - lots of it
- Variety - diversity of the data
    - many different types
- Veracity - quality and origin of data
    - consistency, completeness, integrity, ambiguity
- Value - our need to turn data into something valueable

## Big Data Processing Tools

Hadoop - distributed storage and processing of large datasets
- a node is a single computer, a collection is a cluster
- reliable, scalable, cost-effective solution
- incorporates data formats not traditionally used in data warehouses
- HDFS - runs on multiple commodity hardware over the network
    - splits large files over multiple computers
    - processes can run in parallel
    - replicates file blocks on different nodes to prevent data loss
    - higher availability, better scalability, data locality
    - fast recovery from hardware failures
    - portable across multiple storage devices

Hive - open-source data warehouse for reading writing and managing large data set files that are stored directly in either HDFS or other data storage systems such as Apache HBase
- not suitable for high-write operations
- good for data warehousing tasks such as ETL, reporting, and data analysis

Apache Spark - data processing engine
- good for interactive analytics, streams processing, machine learning, data integration, and ETL
- has in-memory processing which increases speed
- provides interfaces for many programming languages
- can run on stand-alone clustering, or on others
- can access data in a large variety of sources, including HDFS and Hive

# Gathering Data

## Processing for IDing Data
Step 1 - Determine the information you want to collection
- specific information and possible sources of data

Step 2 - Define a plan for collecting data
- establish a timeframe (i.e. procedural vs event based)
- how much data is sufficient for analysis
- define dependencies, risks, mitigation

Step 3 - Determine your data collection methods
- depends on sources, types, timeframe, and volume

Data Quality
- to be reliable, data needs to be...
    - free of errors
    - accurate
    - complete
    - relevant
    - accessible
- you need to define the quality traits, the metrics, and the checkpoints 

Data Governance
- security, regulation, compliances

Data Privacy 
- confidentiality, license for use, and compliance to regulation

## Data Sources

Primary data - information obtained by you from the source
- can be from CRM, applications, etc.
- surveys, observations

Sacondary - information from existing sources
- external databases
- reviews

Third-party - from vendors that are selling data

Sources
- Databases
- Internet
- Social media / interactive platforms
- Sensor data
- Data exchange - voluntary sharing b/w providers and consumers
    - source of third-party data
- Surveys
- Census
- Interviews - good for qualitative
- Observations

## How to Gather and Import Data

SQL - used for relational databases
APIs - can also be used for data validation (zip codes/addresses)
Web Scraping - also RSS
Sensor data - data streams
Data exchanges - platforms, including AWS DataExchange, Crunchbase, Lotame, Snowflake

Importing Data
- must first be placed in a repository, a combined view and interface
- specific repositories are optimized for certain types of data
- ETL tools and data pipelines provide automated functions for processing of importing data
    - talend, informatica, python, r


# Data Wrangling

Iterative process that involves data exploration, transformation, validation, and making it available for credible and meaningful analysis

4 Steps
- Discovery/Exploration
    - understand your data better IRT you use case
    - creating a plan for cleaning, structuring, organizing, and mapping your data
- Transformation
    - structuring, normalizing, cleaning, enriching
        - standardizing formats/schemas
        - joins and unions (combine columns vs combine rows)
    - normalization / denormalization
        - cleaning unused data, reducing redundancy, reducing inconsistency
        - denormalization - combine data from multiple talbes into a single table
    - cleaning - fixes irregularities, biases, nulls, outliers, incompleteness
    - enriching - adding data that makes your data more meaningful
        - adding in datasets
        - adding in metadata
- Validation - checking the quality of data after structuring, normalizing, denormalizing, cleaning, and enriching of data
    - verifying consistency, quality, and security of data
- Publishing - delivering the output of the wrangled data for downstream project needs

Documentation - steps and considerations

## Tools for Data Wrangling

Spreadsheets
- Power Query for Excel
OpenRegine
- open-source
- can import and export in a wide variety of formats
- offers menu-based operations
Google DataPrep
- fully managed, run in the cloud
- can automatically detect anomalies and suggest next steps
Watson Studio Refinery
- detects types and classifications, also enforces data governance automatically
Trifecta Wrangler
- cloud-based, takes messy data and cleans and rearranges it into data tables
Python
- Jupyter Notebook, NumPy, Pandas
R
- Dplyr, Data.table, jsonlite (good for parsing API calls)

## Data Cleaning

Cleaning is only a process of wrangling

Workflow
- Inspection
    - detect issues and errors
    - validate against rules and constraints
    - profiling data to inspect source data
        - profiling inspect source data and relationships, as well as anomalies or inconsistencies
    - visualizing data using statistical methods
Data issues
- missing values
- imputate - calculate the missing value based on statistical values
- duplicates
- irrelevant data
- outliers
- syntax errors

Verification
- inspect results to establish effectiveness and accuracy achieved as a result of the cleaning
- 

Cleaning can involve data type conversion as well
Standardizing data is used to maintain formats for measurements

Should document all steps taken when cleaning







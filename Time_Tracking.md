# **Data Engineering Challenge - Time Tracking Log**

# Day 1 :

### Time Data

* Begin: 21h00 (UTC-3)

* End: 23h00 (UTC-3)

* **Time Spent:** 2h00


# Day 2 :

### Time Data

* Begin: 18h29 (UTC-3)

* End: 23:56 (UTC-3)

* **Time Spent:** 5h30


# Day 3 :

### Time Data (Part 1)

* Begin: 12h45 (UTC-3)

* End: 17h00 (UTC-3)

* **Time Spent:** 4h15


### Time Data (Part 2)

* Begin: 20h00 (UTC-3)

* End: 23h10 (UTC-3)

* **Time Spent:** 3h10


# **Total Time:**

* Day 1: 2h00

* Day 2: 5h30

* Day 3 (Part 1): 4h15

* Day 3 (Part 2): 3h10

**TOTAL TIME:** 14h55

(Time Budget: 15h00)



# **Activities (Done):**


- **Everything (code, docs, etc.) are to be in version control. It's up to you how you'd like to organize it just as long as you can add me to a repo.**

GitHub repository for version control;


- **Implement an HTTP server using any technology you'd like.**

Imported Swagger directives into a Python Flask HTTP Server;


- **Implement the infrastructure in a one-off way by just using the AWS console. Clicking buttons FTW!**

Done and running!


- **Deploy the http server to the cloud.**

Deployed Flask into AWS EC2 via SSH + Git with shell scripts for management;


- **Write good documentation.**

Documentation.md file documents the development process.


- **Have some very basic tests showing the system works.**

Tests via Swagger UI confirm all HTTP Requests are working. Future: implement Pytest.


- **Implement the infrastructure in terraforms so that it can be deployed in as few commands as possible.**

Terraform configured for deployment of: AWS EC2, AWS Kinesis Firehose, AWS S3 Bucket, AWS Networking (VPC, Gateway, Route Table, Subnets, Security Groups).

Small issue found when configuring Firehose parameter **DeliveryStreamType = "DirectPut"**. Future: fix this and connect pipeline.

# **Activities (To-Do):**

- **Implement ansibles.**

Future: Implement ansibles to replace SSH + Git management. Shell scripts already exist and should make this process easier (script workflow has been mapped).

### Detailed Notes on AWS Load Balancers

#### Introduction to AWS Load Balancers
AWS load balancers are crucial for distributing incoming application traffic across multiple targets, such as EC2 instances. They help ensure high availability, fault tolerance, and scalability.


#### Importance of Load Balancers
Load balancers prevent a single point of failure and help manage traffic load effectively. For instance, if you deploy a game on an EC2 instance and it becomes popular, a single instance might not handle the increased traffic. Adding more instances and using a load balancer can distribute the load, improving user experience by preventing slowness and downtime.

#### Types of AWS Load Balancers
AWS supports three types of load balancers:
1. **Application Load Balancer (ALB)**
2. **Network Load Balancer (NLB)**
3. **Gateway Load Balancer (GWLB)**

### Concepts to Understand Before Diving into Load Balancers
1. **What is a Load Balancer?**
2. **How a Packet Flows from Client to Server (OSI Model)**

#### What is a Load Balancer?
A load balancer distributes incoming application or network traffic across multiple targets. It can help ensure that no single instance bears too much load, thereby improving the overall performance and availability of the application.

#### OSI Model and Packet Flow
Understanding the OSI model is crucial because different load balancers operate at different layers. Here’s a simplified breakdown of the seven layers:
1. **Layer 7 - Application Layer:** Deals with application-specific functions such as HTTP, FTP.
2. **Layer 6 - Presentation Layer:** Manages data translation and encryption (e.g., SSL/TLS).
3. **Layer 5 - Session Layer:** Handles session management.
4. **Layer 4 - Transport Layer:** Manages end-to-end communication, reliability, and flow control (e.g., TCP/UDP).
5. **Layer 3 - Network Layer:** Routes packets across networks (e.g., IP).
6. **Layer 2 - Data Link Layer:** Manages node-to-node data transfer (e.g., MAC address).
7. **Layer 1 - Physical Layer:** Deals with the physical connection (e.g., Ethernet cables).

### AWS Load Balancer Types and When to Use Them

#### Application Load Balancer (ALB)
- **Layer:** Operates at Layer 7 (Application Layer).
- **Use Case:** Best for HTTP and HTTPS traffic and provides advanced routing, such as host-based or path-based routing.
- **Features:**
  - Path-based and host-based routing.
  - SSL termination.
  - WebSocket support.
  - HTTP/2 support.
- **Example:** Use ALB for a website like amazon.com where different paths (e.g., /payments, /login, /products, /cart) route to different services.


#### Network Load Balancer (NLB)
- **Layer:** Operates at Layer 4 (Transport Layer).
- **Use Case:** Ideal for TCP, UDP, and TLS traffic where extreme performance and low latency are required.
- **Features:**
  - Handles millions of requests per second.
  - Low latency.
  - Static IP support- Provides a static IP address for the load balancer, useful for whitelisting and integration with other services.
  - TLS termination.
  - Zonal isolation- Operates at the connection level (Layer 4) and supports failover across Availability Zones.
- **Example:** Real-time online gaming or video streaming services requiring high throughput and low latency.

##### Example:

A user requests access to a website. The ALB inspects the HTTP headers and routes the request based on the URL path to the appropriate backend server.
In contrast, an NLB would route the request based on IP address and port number, ensuring minimal latency.

#### Gateway Load Balancer (GWLB)
- **Layer:** Operates at Layer 3 (Network Layer) and Layer 4 (Transport Layer).
- **Use Case:** Used for deploying, scaling, and managing virtual appliances like firewalls, intrusion detection and prevention systems.<br/>
Organizations that need to secure traffic with a firewall or manage traffic through a VPN.
- **Features:**
  - Integrates with AWS Firewall Manager.
  - Provides high availability.
  - Simplifies deployment of third-party network appliances.
- **Example:** Use GWLB for security appliances like virtual firewalls to inspect and filter traffic before it reaches your application.<br/>
A financial institution needing to secure traffic with an intrusion detection system (IDS).



### Load Balancing Techniques
- **Round Robin:** Distributes traffic equally among all servers.
- **Weighted Round Robin:** Distributes traffic based on server weight (capacity).
- **Least Connections:** Routes traffic to the server with the least active connections.
- **IP Hash:** Routes traffic based on client IP.

### Summary
- **ALB:** Best for HTTP/HTTPS traffic with advanced routing.
- **NLB:** Best for high-performance, low-latency TCP/UDP applications.
- **GWLB:** Best for deploying and managing virtual network appliances.

### Best Practices
1. **Security:** Always use secure connections (HTTPS/TLS).
2. **Scaling:** Use auto-scaling groups for backend instances.
3. **Health Checks:** Configure health checks to ensure traffic is only routed to healthy instances by LB.
4. **Monitoring:** Use CloudWatch to monitor load balancer metrics.


### Practical Considerations
**High Availability**: Load balancers help achieve high availability by distributing traffic and ensuring no single point of failure.
**Scalability**: They allow applications to scale horizontally by adding or removing instances based on load.
**Security**: Load balancers can offload SSL termination and provide a front line of defense against DDoS attacks.

### Real-World Example
For a video streaming platform like YouTube, using an NLB is beneficial due to its low latency and high throughput capabilities. However, for a web application requiring content-based routing and SSL offloading, an ALB would be more appropriate.

By understanding and utilizing the appropriate AWS load balancer type, you can ensure your applications are highly available, scalable, and resilient to failure.


![image](https://github.com/HimanshuMishra123/aws-devops-zero-to-hero/assets/164254902/47904922-0246-4ae6-aa31-6b8837302918)

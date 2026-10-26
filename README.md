# CS 340 – Client/Server Development

## Project Two: Grazioso Salvare Animal Rescue Dashboard

### Project Overview

For this project, I developed an interactive dashboard for Grazioso Salvare, an organization that identifies dogs suitable for search-and-rescue training. The dashboard uses animal shelter data from the Austin Animal Center to help the organization identify dogs that meet specific rescue training requirements.

The project involved using Python, MongoDB, Dash, Plotly, and other visualization tools to create a functional dashboard that allows users to filter animal records, view relevant information in a table, and visualize animal locations on an interactive map. I also developed a CRUD Python module to connect the application to the MongoDB database.

This project strengthened my understanding of database management, application development, and the importance of creating software that meets real-world client requirements.

### 1. How do you write programs that are maintainable, readable, and adaptable?

When writing programs, I focus on creating code that is organized, readable, reusable, and easy to modify. I accomplish this by using descriptive variable names, meaningful comments, modular programming techniques, and consistent coding practices. I also separate different responsibilities within an application to make troubleshooting and future updates easier.

In Project One, I developed a CRUD Python module that provides methods for creating, reading, updating, and deleting records in a MongoDB database. During Project Two, I reused this module to connect my interactive dashboard to the animal shelter database. This approach allowed me to separate database operations from the dashboard's user interface.

One major advantage of this design was that I did not need to rewrite the database connection and retrieval functionality when developing the dashboard. Instead, I could focus on implementing interactive features, including rescue-type filters, data tables, and geographic visualizations. Separating these components also made the application easier to maintain because database-related changes could be made independently of the dashboard interface.

In the future, I could reuse or expand this CRUD Python module for other applications requiring MongoDB database interactions, such as inventory management systems, customer information platforms, or employee management applications. This experience demonstrated the importance of developing reusable software components that support efficient and scalable application development.

### 2. How do you approach a problem as a computer scientist?

As a computer scientist, I approach problems by identifying the requirements, breaking complex tasks into manageable components, developing solutions, and testing the results. I believe it is important to understand the client's needs before selecting the appropriate technologies or designing an application.

For the Grazioso Salvare project, I began by examining the database requirements and understanding how the organization needed to identify dogs suitable for different search-and-rescue activities. The dashboard needed to support filtering for water rescue, mountain or wilderness rescue, and disaster or individual tracking. Each category required specific animal characteristics, including breed, age, and other relevant information.

After understanding these requirements, I used MongoDB queries to retrieve appropriate records and connected the database to the dashboard using my CRUD Python module. I then developed interactive dashboard components that allowed users to select rescue categories and view the corresponding animal information.

This project differed from many of my previous programming assignments because it required integrating multiple technologies into one application while addressing the needs of a specific client. Rather than focusing only on writing code to solve an isolated problem, I needed to consider database structure, user interaction, data visualization, and the overall functionality of the application.

In future projects, I will continue using a structured problem-solving approach that includes requirement analysis, database planning, modular development, testing, and documentation. I would also use techniques such as data validation, query optimization, and database indexing when appropriate to improve application reliability and performance.

### 3. What do computer scientists do, and why does it matter?

Computer scientists design, develop, analyze, and improve technological solutions that help individuals and organizations solve problems. Their work includes software development, database management, cybersecurity, artificial intelligence, data analysis, and system optimization. Computer scientists play an important role in making technology more efficient, reliable, and accessible.

The Grazioso Salvare project demonstrates how computer science can support an organization's daily operations and decision-making processes. By creating an interactive dashboard connected to a database, I developed a tool that allows users to search and analyze animal shelter records more efficiently.

Instead of manually reviewing large amounts of animal information, Grazioso Salvare can use the dashboard to filter records according to specific rescue training requirements. The data table and geographic visualization features also make it easier to understand and interpret the available information.

This type of application can help organizations save time, reduce manual effort, and make more informed decisions. In the case of Grazioso Salvare, identifying suitable dogs more efficiently could support the organization's search-and-rescue training efforts.

Overall, this project helped me recognize how computer scientists use programming, databases, and analytical thinking to develop practical solutions. It also reinforced my interest in creating software that improves organizational efficiency and provides meaningful benefits to users.

### Conclusion

Completing the Grazioso Salvare dashboard project provided valuable experience in Python programming, MongoDB database management, and interactive application development. I learned how to integrate database operations with user interface components while following software development practices that promote maintainability and reusability.

The knowledge and technical skills I gained throughout this course will help me approach future software development projects with greater confidence. This project also serves as an example of my ability to apply computer science concepts to real-world challenges and develop solutions based on client requirements.

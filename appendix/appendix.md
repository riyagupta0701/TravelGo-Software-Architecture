## 16 Appendices:

## Appendix A: Personas

Personas are defined as fictional representations of users aimed to represent the diverse range of individuals
interacting with a specific application. They are used in order to observe and simulate a user’s interaction
with the platform once completed. Ultimately, constructing different personas can help identify weak points
and edge cases within the platform. In our case, all personas are assumed wto be unfamiliar with any programming knowledge.

### A.1 Tourist/Traveller

This persona represents a typical travel enthusiast, visiting different countries and attractions. Each tourist as a bucket-list with attractions they decide to visit for that country. Tourists interact with each other, with guides, obtain discounts and discover new attractions.

### A.2 Local Business Owner (Sponsor/Business Partner)

Since the app features discounts for various restaurants or souvenir shops, this persona represents local shop-owners that wish to improve their business. They process the monetary fee through the platform and in return offer the tourists a discount, voucher or even a free souvenir. Furthermore, they are also considered local sponsors since they ultimately wish for publicity for their business.

### A.3 Travel Agent

This persona represents a travelling expert with extended knowledge about various attractions. They help clients plan, book, and customize trips by offering professional advice on destinations, accommodations, and experiences.

### A.4 (Potential) External Sponsor

A sponsor is typically a brand, or local business which seeks visibility for their product among any individuals. They want to attract and engage individuals through gamified experiences and offered promotions in exchange for brand exposure.


## Appendix B: User Stories

A user story is a brief description of a feature that a persona requires in the system. Furthermore, the overall benefit of this feature for the system’s development is also presented.

| User Story ID | User Story |
|--------------|------------|
| US1           | As a Tourist, I wish to be able to see information for each attraction. |          
| US2           | As a Tourist, I wish to be able to answer cultural questions about an attraction to improve my knowledge and receive points for completing a quiz per attraction. |          
| US3           | As a Tourist, I wish to be able to participate in a country's league for the ultimate traveling champion. |          
| US4           | As a Tourist, I want to engage with other travellers through a community platform. |          
| US5           | As a Tourist, I want to be able to suggest new attractions in a country and earn points if my suggestion is validated. |          
| US6           | As a Tourist, I wish to be able mark attractions as visited and cross them from my bucket-list. |          
| US7           | As a Tourist, I want the platform to create a traveling plan for me, which I then will be able to export the external map applications. |          
| US8           | As a Tourist, I want the platform to suggest nice local and traditional restaurants and open-area places when I am nearby and attraction. |          
| US9           | As a Tourist, I want to pay extra for this platform to suggest me available accommodations near my current attraction that are also not crowded. |          
| US10           | As a Tourist, I want to pay extra to remove pop-up ads. |          
| US11           | As a Local Business Owner, I want the platform to recommend my business through pop-up ads. |          
| US12           | As a Local Business Owner and Sponsor, I want the platform to offer 5% discounts for all platform users to increase publicity. |          
| US13           | As a Local Business Owner, I want the free earned souvenir to have a representative picture on the platform. |          
| US14           | As a Local French Restaurant Owner, I want the platform to recommend my business at the end of the quizzes for traditional places. |          
| US15           | As a Travel Agent, I want offer city tours through TravelGo, for my clients to play along and for me to stand out from standard booking platforms. |          
| US16           | As a Travel Agent, I want the platform to highlight premium guided tours or special events in collaboration with my agency in order to promote my business. |          
| US17           | As an External Sponsor, I wish to financially support the platform's development in exchange for exposure. |          

## Appendix C: Recommended Architectural Patterns

Below is a table showcasing appropriate architectural patterns for the implementation of the TravelGo system. The research for suitable microservice patterns was heavily relying on Ahmad's article [[10]](#10).

| Pattern Name | Pattern Description |
|--------------|---------------------|
| API Gateway           | Serves as a single entry point for client requests, routing them to appropriate microservices and safely manages concerns such as authentication. |          
| Service Discovery (Service Registry)  | Allows microservices to dynamically find and communicate with each other by registering themselves and maintaining a central registry. |          
| Circuit Breaker           | Prevents cascading failures such that each service is independently connected and in case of failure the entire system remains running with only the failing one being shut down. |          
| Retry Pattern      | Automatically retries failed operations in an attempt to fix errors. |          
| Event Sourcing Pattern   | Stores state changes as a sequence of events which can be replayed to reconstruct the system's state at any point in time. |          
| Event driven      | Uses events as the primary means of communication between services, allowing for asynchronous actions. |          
| CQRS           | Separates read and write operations into independent models to optimize performance, scalability, and complexity. |          
| Sidecar Pattern  | The system deploys auxiliary components alongside their primary service to account for logging or configuration concerns.  |          
| "Smart Endpoints, Dumb Pipes"  | Ensures that the logic is maintained in the services only and their connections (pipes) remain with little to no complexity implemented. |          
| Shadow Deployment   | Runs a new version of a service in parallel (a "shadow") without affecting user and or the network's traffic, allowing for easier testing. |          
| Stateless Services   | Ensures that services do not store the state of client sessions locally, thus enabling them to be scaled and replaced independently. |
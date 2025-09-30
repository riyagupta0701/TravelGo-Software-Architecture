<h1 align = "center">TravelGo!</h1>
<h3 align = "center">Team 11 <br> Aník van Deursen, Riya Gupta, Radha Mujumdar, Diana Todoran</h3>

## 1 Introduction
<!-- 
• Adopt selection of techniques (with references) to analyze 
  problem domain and context in which system operates
• Structure problem domain (= design) and offer 
  initial ideas on concept architecture (= solution)
• Motivate choice of techniques
• Evaluate suitability of techniques used and assess what extra 
  insights additional techniques could offer (with references) 
-->

### 1.1 Problem Statement
Travelling is one of those things that everyone loves. Seeing new places, learning about cultures and tasting the finest of cuisines is an experience unlike any other. However, sometimes it can be quite challenging to see as much of a site as we would like. Fully engaging with the culture, history and seeing all of the highlights and hidden spots is almost impossible if you only have limited time. 

Another challenge is connecting with other travellers. Tourist, especially solo-travellers, can have difficulty finding like-minded people. Because of this they might not create meaningful connections during their travels, which is unfortunate since exploring a city is even more fun with others!

### 1.2 Context & purpose
We want to create an interactive digital platform that makes travelling easier and more fun for both group and solo travellers across various countries: TravelGo. Central to the platform is a map with all of the tourist attractions, including hidden spots. The platform aims to enrich cultural engagement with competitive games (for example quiz competitions) with a reward system through leaderboards. To make this competition fun for both inexperienced and experienced travellers, the platform uses a rating system with leagues. Users can additionally earn points by going to an attraction and thus ticking it off their bucket list. These points can be used to for example get a discount on entry fees or to get an exclusive souvenir.

Another main part of TravelGo is making it easier for travellers to engage with each other. To encourage tourist interaction, the platform will have a chatroom. This chatroom helps travellers to meet new people that are at the same location. Users can also post new or hidden attractions that they recommend to others. Because of this, tourist will know which attractions they should definitely visit.

## 2 Wardley Map
![](WardleyMap.png)
<p style="text-align: center;">Figure 2.1 : Wardley map</p>

**Genesis** : This space contains novel, experimental features like side quests, cultural quizes and souvenir based rewards which are not yet mainstream in the travel tech domain. They provide differentiation, but also present a high risk of adoption and design. <br>
**Custom Built**: Features like leaderboards and points system are placed here. While interactive platforms are popluar in other domains like fitness and education, applying it specifically to cultural travel remains relatively bespoke. These features distinguish TravelGo from commodity travel apps but are less risky than Genesis elements. <br>
**Product Stage**: More well known features such as community chatrooms and posting comments fall under this category. These are standard capabilities available in many social or booking apps, but TravelGo customizes them for cultural travel contexts. They are visible to users but do not offer radical innovation. <br>
**Commodity Stage**: Underlying infrastructure such as digital maps, location pinning, user accounts and APIs are considered commodity. They are invisible to end-users and widely available through third-party providers like Google Maps. TravelGo does not attempt to innovate here but instead rely on stable, low-cost services. <br>

## 3 Market Research

To identify opportunities for innovation, it is useful to examine the existing players in the travel tech market. The table below presents a comparative analysis of these competitors, outlining their strengths, weaknesses, and potential gaps.

| Serial No. | Competitor | Strengths | Weaknesses | Opportunity for us |
|--------|------------|-----------|------------|---------------------|
| 1 | **TripRanger** | Gamifies travel, fun challenges | Limited user base, not mainstream, focus mostly on gamification rather than deep cultural immersion | We can combine interactivity and cultural depth, making it more meaningful |
| 2 | **Polarsteps** | Very popular, creates a visual travel journal, great for reliving your travel experiences. Helps share trips with friends and family | Mostly passive (recording, not interacting); limited social engagement beyond sharing | We add interactivity, side quests, community building |
| 3 | **Withlocals** | Popular; focused on authentic cultural experiences by connecting with locals/guides | Paid/expensive; depends heavily on guide availability; no gamification or community | Make authentic culture accessible and community driven |
| 4 | **Viator** | Huge catalog of tours & activities | Overly commercial and not personalized, lacks interactive features | Focus on personalized, fun challenges and cultural immersion rather than generic tours |
| 5 | **Komoot** | Expertise in outdoor navigation and route planning | Very niche (outdoors only) | Add cultural challenges with a social community |
| 6 | **Mapstr** | Save and share favorite places easily | More like a utility app (maps), lacks engagement, no gamification | Build on map sharing, but with interactive quests, culture and competition | <br>
| 7 | **Google Maps** | Massively popular for navigation, locating places | Lacks the interactive aspect | We add interactivity and culutral immersion | <br>
<p style="text-align:center;">Table 3.1 : Competitor Analysis</p>

### 3.1 Key Insights

#### Is there demand?  
Market trends indicate that travellers increasingly seek experiences over mere sightseeing. Therefore, platforms that are interactive and community-driven are especially popular among younger travellers nowadays.[[2]](#2)[[3]](#3)[[4]](#4)

#### What’s missing in current solutions?  
- Most travel apps focus on either utility (planning, booking) or authenticity (guided tours).  
- Few apps combine an interactive, culturally immersive experience with community building.  
- Existing solutions often lack interactivity, offline usability, or gamified side quests.  

#### How TravelGo fills that gap  
- Integrates interactive, culturally immersive experiences with community engagement into a single platform.  
- Enables users to complete side quests, join challenges, and earn rewards while exploring off-beat locations.  
- Promotes social discovery by connecting travellers nearby.  
- Built with an offline-first architecture, considering real traveller needs such as spotty internet and battery constraints.

## 4 Challenges

**I. Data Privacy & Trust** : Data privacy and trust are critical concerns for TravelGo, as the platform collects personal information such as names, locations, and travel history. Mishandling this data could result in legal issues and a loss of customer trust. However, several ambiguities arise, such as determining how much data should be collected, finding the right balance between personalization and privacy, and managing cross-border compliance. From an architectural perspective, the system must implement data minimization by collecting only what is necessary, incorporate strong consent management, and ensure secure data storage and transmission. Additionally, regional data hosting may be required to meet compliance regulations.

**II. Cultural Sensitivity & Representation** : TravelGo promotes cultural quests and hidden gems, but what one traveler considers a “hidden gem” could, in fact, be a sacred site or a sensitive local tradition. Such misrepresentation risks community backlash and even legal consequences. This raises ambiguities around who decides what is “authentic” enough to feature and how to avoid cultural appropriation or trivialization. Architecturally, the platform may require robust content vetting workflows, potentially involving local validators or approval pipelines for sensitive submissions. Flexible data models will also be needed to support metadata tagging of cultural content such as marking items as sensitive, sacred, or family-friendly, along with the ability to enable regional customization where necessary.

**III. Technical Constraints** : Travelers often face unreliable connectivity, yet TravelGo’s core features such as locating pins, chat, and quests may rely heavily on online services. This raises ambiguities around which features should remain functional offline and how much data can reasonably be cached on a device without draining storage or battery. Through an architectural lens, the system may need to adopt an offline-first design, ensuring that critical functions remain usable without constant connectivity. In particular, GPS tracking without internet access would depend on operating system support and offline map APIs.

**IV. Community Moderation & Safety** : TravelGo’s chatrooms and commenting features are central to its social experience, but like most online community spaces, they can quickly become targets for spam, harassment, scams, or inappropriate content. This introduces ambiguities around whether moderation should rely on AI and keyword blocking or be led by human moderators, how to enforce community rules across diverse cultures and languages, and whether moderation should be centralized or distributed.From a design point of view, this creates the need for scalable content moderation pipelines, along with careful handling of flagged content since its storage and processing bring compliance and legal liabilities. At the same time, balancing low latency for real-time chat with effective filtering poses significant technical challenges.

**V. Ecosystem Dependencies** : TravelGo relies on third-party APIs for critical functionalities such as maps and login, but this dependency introduces several uncertainties. Providers may change pricing models, discontinue services, or have limited availability in certain regions. This raises the question of whether to design for multi-provider fallback or accept the risks of locking into a single provider. From an architectural standpoint, it becomes important to introduce abstraction layers rather than hardcoding to any one API, consider vendor diversity to reduce reliance on a single source, and actively monitor latency and reliability across providers to ensure a consistent user experience.


## 5 Stakeholders

Travellers create demand by seeking personalisation and meaningful connections, gravitating toward the cultural, recreational, and community-driven offerings available on the platform. They engage with attraction sites and redeem discounts at local businesses, boosting visitor numbers and generating higher revenue for these stakeholders while promoting their trade. Management works closely with regulatory authorities and tourism boards to ensure compliance and safety. Strengthening the platform’s visibility, travel communities and influencers amplify positive experiences through information sharing and marketing. Together, TravelGo delivers reliable, user-centric travel solutions while balancing the needs of customers, local communities, and the broader ecosystem.

### 5.1 Primary Stakeholders

- Tourists and Travellers
  - Main users of the platform
  - Engage in competitive games, meet like-minded individuals and be interested in cultural enrichment
- Attraction Sites
  -  Higher footfalls and visitor engagement resulting in an increase in ticket sales
-  Local Businesses
   -  Advertisements and partnerships will gain more exposure, eliciting profits
   -  Support special offers and discounts

### 5.2 Secondary Stakeholders

- Government and Tourism Boards
  - Boost in tourism while ensuring compliance of the local laws
  - Control the digital platforms, tourism, and safeguarding the cultural
- Local Communities
  -  Cultural representatives who gain from more interactions and business from tourists
  -  Might be worried about cultural sensitivity
-  Investors and Sponsors
   -  Support financially and expecting returns in the form of partnerships, advertisements, subscriptions, and even positive publicity
  
### 5.3 Tertiary Stakeholders

- Travel Agencies and Tour Operators
  - Competitors or can be potential partners
- Online Travel Communities and Influencers
  - Increase online engagement and positive word of mouth through social media 

<br>

The power/interest grid is used to classify stakeholders according to their influence and level of engagement. High-power, high-interest stakeholders such as travellers and attraction owners are closely managed since they are the core users. Tourism boards and regulators have high power but lower day-to-day interest, requiring consultation occasionally. Communities, influencers, and competitors have lower power but varying levels of interest, monitored for promotion and market positioning.

![](PowerInterestGrid.png) 
<p style="text-align: center;"> Figure 5.1: Power / Interest Grid </p>


## 6 Personas

Personas are defined as fictional representations of users aimed to represent the diverse range of individuals
interacting with a specific application. They are used in order to observe and simulate a user’s interaction
with the platform once completed. Ultimately, constructing different personas can help identify weak points
and edge cases within the platform. In our case, all personas are assumed wto be unfamiliar with any programming knowledge.

### 6.1 Tourist/Traveller

This persona represents a typical travel enthusiast, visiting different countries and attractions. Each tourist as a bucket-list with attractions they decide to visit for that country. Tourists interact with each other, with guides, obtain discounts and discover new attractions.

### 6.2 Local Business Owner (Sponsor/Business Partner)

Since the app features discounts for various restaurants or souvenir shops, this persona represents local shop-owners that wish to improve their business. They process the monetary fee through the platform and in return offer the tourists a discount, voucher or even a free souvenir. Furthermore, they are also considered local sponsors since they ultimately wish for publicity for their business.

### 6.3 Travel Agent

This persona represents a travelling expert with extended knowledge about various attractions. They help clients plan, book, and customize trips by offering professional advice on destinations, accommodations, and experiences.

### 6.4 (Potential) External Sponsor

A sponsor is typically a brand, or local business which seeks visibility for their product among any individuals. They want to attract and engage individuals through gamified experiences and offered promotions in exchange for brand exposure.


<!---
## Epics

In this section, we list the epics, along with the corresponding description. Each epic has its features, which
further contribute to the User Stories. <span style="color:red">TBA later when further developed</span>.

--->

## 7 Features

Features are distinct pieces of functionality that deliver value to users. They define what the software can do and are often used to plan and develop the product throughout its lifecycle.

| Feature ID | Feature Description|
|-----------|------------|
| F1         | Maintain an individual user bucket-list of attractions.          |        
| F2         | Display a map with available countries and available attractions in each country.       |        
| F3         | Maintain a community chatroom for attraction discoveries and user interactions.       |        
| F4         | Display advertisements.          |              
| F5         | Allow for premium features. (Let the user know when there are discounts for accommodation)        |        
| F6         | Keep track of the user's daily quiz score and their placement in the leaderboard. |        
| F7         | Reward the top competitors of the leaderboard with discounts, vouchers or free souvenirs.         |
<p style="text-align: center;">Table 7.1: List of features that will be implemented for the final product.</p>

## 8 Use Case Scenarios

Use case scenarios explain how a user works with a system to accomplish certain tasks or objectives. They
outline the steps needed to achieve a set objective and also help define system requirements, derived from
the user stories, which can be found in the Appendix A.

| Use Case ID | Use Case Description |
|--------------|------------|
| UC1          | Automatically display a map of available countries. |          
| UC2          | Automatically display a map of available attractions for the selected country. |          
| UC3          | Create a traveling plan for a given number of visiting days. |          
| UC4          | Create a sharable link of the traveling plan. |          
| UC5          | Allow users to cross-off visited attractions from the plan/bucket-list. |          
| UC6          | In the case of quizes, the platform must offer a selection of questions, weighted in points. The summed points increase the user's daily score for the leaderboard. |          
| UC7          | Determine the user's reward based on their score. |          
| UC8          | Display advertisements for internal and external sponsors. |          
| UC9          | Display available discounts for internal and external sponsors. |                   
| UC10          | Process shop fee for earned souvenir by the user. |          
| UC11          | Maintain a hidden gem list of attractions. |      
| UC12          | List various restaurants or outdoors environments for nearby attractions. | 
| UC13          | (In case of premium) Process subscription fee for unlocking premium for the user's account. |          
| UC14          | (In case of premium) display a list of available accommodations. |          
| UC15          | (In case of premium) Remove advertisements and any sort of advertisement. |          
<p style="text-align: center;">Table 8.1: List of use case scenarios that will be implemented for the final product.</p>

<!---
## Requirements

Requirements are documented descriptions a software system's tasks that it can perform or qualities
it should possess to fulfill stakeholders’ needs. Furthermore, they also provide key steps for solving
the user stories.
--->

## 9 Quality Attributes
Quality attributes describe desirable properties of a system.
For creating TravelGo we want to consider the following elements:

**Time to market**: It is essential to release our product at the right time. Most people travel around the summertime, therefore the platform should be on the market before summer. TravelGo could also be released while it is still imperfect. In that case, since it would be possible to get feedback from users, it would be easier to see which features people like. We could then fine-tune and build on those features and discard the ones that people did not use much.
\
\
 **Modularity**: Since the platform will have distributed deployment, TravelGo needs to use modules. Modularity is also important for parallel development and incrementally building. 
\
\
**Performance**: TravelGo should not take a long time to respond, since this will annoy users and might make them not want to use the app. We also want the system to be able to take many requests at the same time.
\
\
**Scalability**: At first, TravelGo will not have a lot of users. Of course we hope to increase this amount over time. Because of this, the architecture should be designed for growth.
\
\
**Usability**: The user interface should be very convenient and intuitive to use. It should be easy to learn for first-time users and memorable for returning users. Since the platform will be available in many different countries, it should be convenient to use in all those countries, including different language options.
\
\
**Serviceability**: The system should be easy to maintain. A lot of new tourist attractions will be added over time, and the user should not have to update the app every time an attraction is added. Since the platform is intended for users all around the world, there is always a timezone that suffers if we do maintenance work. Therefore we want to have to do as little maintenance as possible.
\
\
**Availability**: The system should be functioning correctly 24/7, since our users are in many different timezones, which means that the platform is always in use.
\
\
 **Defensibility**: Since we work with our users personal data and have a chatroom functionality, we need to be certain that the system is protected from malicious attacks. Additionally, we need to ensure that no malicious content is posted in the chatroom. It is also important that our data for the tourist attractions is correct, since tourist are more likely to fall for scams.
 \
 \
 **Privacy**: Because TravelGo has access to users' names, locations, and personal conversations in the chatroom, it is important to ensure that our users' personal data is secret and protected.
\
\
**Adaptability**: It is important that our system is extensible, because we want to add new features as the platform becomes more successful. We also want our system to be modifiable, so that the implemented functionality can be changed if needed and we can remove less successful features.
\
\
**Portability**: We want our platform to be available for all systems. If we make the app portable, we can save a lot of costs and effort.
\
\
**Sustainability**: We need to ensure that our product does not become irrelevant in the future, both in technical and economical terms. It is also important to make sure that the platform grows from the start.
\
\
The quality attributes that we primarily want to focus on are **availability**, **performance** and **scalability**.

### 9.1 Trade-offs
For the main quality attributes, there are some trade-offs that we should keep in mind while designing the system:

**Availability vs privacy**: We always want our system to be available for every user. However, this might have impact on the privacy of users. For example, TravelGo utilizes the location of its users. Some users may not want to share their location, which means that certain functionalities of TravelGo would not work for them.
\
\
**Performance vs time to market**: If we want to release TravelGo as soon as possible, it may be difficult to optimize the performance of the platform before the deadline. 
\
\
**Scalability vs defensibility**: TravelGo should be designed for growth of user-base. However, a large user-base all around the world could have an impact on defensibility. For example, if we have a lot of posts in the chatroom, it is more difficult to monitor for malicious intent.
\
\
**Scalability vs performance**: We want TravelGo to have as many users as possible. However, with more users, the performance of the app might go down, especially if the users are from all around the world. 

## 10 Proof of Concept

The proof of concept demonstrates how the platform can bring together travellers and tourism industry workers in one ecosystem. It validates core features such as interactive maps, attraction discovery, user-generated content, and gamification elements like leaderboards. By integrating with external systems (e.g., map services, tourism datasets), the POC shows the feasibility of delivering real-time, location-based recommendations while ensuring engagement through posts, ratings, and rewards.

### 10.1 External Dependencies

The platform relies on several external dependencies to function effectively. Some core services include maps and geolocation APIs (e.g., Google Maps) for navigation, routing, and location tracking. Furthermore, with respect to monetization, the platform depends on payment processors (IDEAL, PayPal, etc). On the technical side, the use of cloud hosting and databases would provide scalability and performance. Additionally, authentication services (Google, Facebook, etc) and communication tools (email/SMS providers) would also be employed to support user management.

For the current proof of concept implementation, we made use of [Leaflet](leafletjs.com) and [openstreetmap](https://www.openstreetmap.org/#map=6/46.45/2.21) to develop the interactive map.
x
### 10.2 System Context Diagram

The C4 System Context Diagram highlights TravelGo’s role within its environment. It shows the platform as the central system interacting with travellers, attraction owners, and several external systems such as map providers, tourism boards, influencers, and competitors. The diagram illustrates key flows of information (e.g. travellers providing personal information, owners submitting attractions, the platform requesting maps) and helps define clear system boundaries and dependencies.

![](ContextDiagram.png)
<p style="text-align: center;">Figure 10.2.1: Context Diagram</p>


## 11 Revenue Model

In order to ensure long-term success for a platform, a sustainable revenue model is essential. The presented system would blend reality exploration with competitive gaming, meaning it can attract tourism-focused partnerships, as well as game-industry monetization.

### 11.1 Revenue Streams

The platform can be supported by income from multiple combined streams presented in the table below.

| Revenue Stream   | Implementation Details | Advantages| Challenges |
| -------------------------------- |-------- | --------- | ----------|
| Free Content / Subscription | Free tier with core features; premium tier unlocks exclusive content | Predictable recurring income; encourages retention   | Requires adequate premium features to justify the cost |
| In-App Purchases  | Cosmetic items, location-based boosts, hints, custom avatars | Transaction-based revenue resulting in immediate revenue from passionate users   | High risk of warping user perception and turning the platform into "pay-to-win" if not balanced |
| Advertising & Sponsorships | Through advertisements, local businesses sponsor the discounts, souveniers and/or events | Transaction-based revenue for non-premium users; Immediate income from sponsors | The advertising cannot be excessive in order to not degrade user experience   |
<p style="text-align: center;">Table 11.1.1: List of viable revenue streams.</p>


Furthermore, since the platform is newly developed, the revenue model should be implemented in progressive stages.
At launch, most of the platform content should remain free to access to build the user base. Additionally, basic in-app purchases for cosmetic reasons can be included. During the next stage, the relation with local business owners would be established, and the platform would begin featuring sponsored restaurants and souvenir shops, as well as custom maps and affiliation with tourist companies in the premium version. Lastly, the final stage could envision production of large-scale events, partnerships with museums from bigger cities and metropolises and potential merch sales.

### 11.2 Risks and Considerations

- User Experience: Excessive monetization risks pushing tourists away, therefore, the free version must remain engaging.
- Fairness: Competitive features must avoid "pay-to-win" dynamics.
- Scalability: Each additional revenue stream increases system complexity. As such, the platform should be built in a modular way so features can be added independently without interfering with existing ones.


## 12 Roadmap
The stages in which the project is carried out can be seen in the roadmap below.

![](Roadmap.png)
<p style="text-align: center;">Figure 12.1: Roadmap</p>

## Bibliography
<a id="1">[1]</a>
Bedjeti, Adriatik; Lago, Patricia; Lewis, Grace A.; De Boer, Remco D.; Hilliard, Rich (1968).
*Modeling Context with an Architecture Viewpoint*.
IEEE International Conference on Software Architecture (ICSA).
<br><a id="2">[2]</a>
Alčaković, S., Pavlović, D., & Popesku, J. (2017). Millennials and gamification: A model proposal for gamification application in tourism destination. Marketing, 48(4), 207–214. https://doi.org/10.5937/markt1704207a 
<br><a id="3">[3]</a>
Gen Z Travel Trends: Statistics, Insights and what it all means for the industry [2025]. (n.d.). Atlys. https://www.atlys.com/blog/gen-z-travel-trends
<br><a id="4">[4]</a> 
Pitrelli, M. (2023, March 27). More millennials are turning 40 — and they’re changing travel as we know it. CNBC. https://www.cnbc.com/2023/03/27/millennials-are-turning-40-and-theyre-changing-travel-as-we-know-it.html
 
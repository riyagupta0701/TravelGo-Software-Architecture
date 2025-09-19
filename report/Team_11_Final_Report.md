# Team 11 - TravelGo!
Aník van Deursen <br>
Riya Gupta <br>
Radha Mujumdar <br>
Diana Todoran

## Introduction
<!-- 
• Adopt selection of techniques (with references) to analyze 
  problem domain and context in which system operates
• Structure problem domain (= design) and offer 
  initial ideas on concept architecture (= solution)
• Motivate choice of techniques
• Evaluate suitability of techniques used and assess what extra 
  insights additional techniques could offer (with references) 
-->

### Problem Statement
Travelling is one of those things that everyone loves. Seeing new places, learning about cultures and tasting the finest of cuisines is an experience unlike any other. However, sometimes it can be quite challenging to see as much of a site as we would like. Fully engaging with the culture, history and seeing all of the highlights and hidden spots is almost impossible if you only have limited time. 

Another challenge is connecting with other travellers. Tourist, especially solo-travellers, can have difficulty finding like-minded people. Because of this they might not create meaningful connections during their travels, which is unfortunate since exploring a city is even more fun with others!

### Purpose
We want to create an interactive digital platform that makes travelling easier and more fun for both group and solo travellers across various countries: TravelGo. Central to the platform is a map with all of the tourist attractions, including hidden spots. The platform aims to enrich cultural engagement with competitive games (for example quiz competitions) with a reward system through leaderboards. To make this competition fun for both inexperienced and experienced travellers, the platform uses a rating system with leagues. Users can additionally earn points by going to an attraction and thus ticking it off their bucket list. These points can be used to for example get a discount on entry fees or to get an exclusive souvenir.

Another main part of TravelGo is making it easier for travellers to engage with each other. To encourage tourist interaction, the platform will have a chatroom. This chatroom helps travellers to meet new people that are at the same location. Users can also post new or hidden attractions that they recommend to others. Because of this, tourist will know which attractions they should definitely visit.

### Context
TravelGo is mainly of value for travellers and tourism industry workers: for example attraction or restaurant owners.
The following information is needed from the environment:
- An up-to-date map
- Data about tourist attractions
  - Well known attractions
  - Lesser known attractions provided by owners and tourists

\
Context identification consists of four parts: platform, user and application context [[1]](#1).
- Platform: TravelGo will be a mobile app, available on apple and android. Users need to be connected to the internet to use TravelGo.
- User context: TravelGo uses personal information (name, interests) and the location of users.
<!-- TODO: DEPENDENCIES: Application context
  - External software context
  - External service context
  - Infrastructure context
  - External Systems context
  - Physical context -->
- Organizational context: discussed in chapter [Stakeholders](#stakeholders).

<!-- Context diagram (c4 model)? -->

#### External risks
Since many travelling apps have been created ([Market Research](#market-research)), TravelGo does not have a lot of risks. There is a lot of reliable knowledge available. 

The main risks are the following:
- Correct information: TravelGo depends on information supplied by tourists and organizations. Since the platform will be available in multiple countries, it is difficult to examine all of the information.
- Privacy: TravelGo has access to the location and personal information of its users.
- External dependencies: TravelGo makes use of open source software.

## Market Research

### Project Overview

TravelGo is an interactive travel companion platform that combines cultural immersion, social networking, and fun challenges to turn every trip into an adventure.

### Target Audience

- **Backpackers / Solo travellers** who are seeking to be part of a community and want to find off-beat ideas.  
- **Young professionals / Digital nomads** who are looking for meaningful cultural immersion, not just sightseeing.  
- **Adventure seekers**, motivated by challenges, exploration, competition.  
- **Families or groups** looking for activities / side-quests which everyone can enjoy.  

### Competitor Analysis

| Sr No. | Competitor | Strengths | Weaknesses | Opportunity for us |
|--------|------------|-----------|------------|---------------------|
| 1 | **TripRanger** | Gamifies travel, fun challenges | Limited user base, not mainstream, focus mostly on gamification rather than deep cultural immersion | We can combine interactivity and cultural depth, making it more meaningful |
| 2 | **Polarsteps** | Very popular, creates a visual travel journal, great for reliving your travel experiences. Helps share trips with friends and family | Mostly passive (recording, not interacting); limited social engagement beyond sharing | We add interactivity, side quests, community building |
| 3 | **Withlocals** | Popular; focused on authentic cultural experiences by connecting with locals/guides | Paid/expensive; depends heavily on guide availability; no gamification or community | Make authentic culture accessible and community driven |
| 4 | **Viator** | Huge catalog of tours & activities | Overly commercial and not personalized,lacks interactive features | Focus on personalized, fun challenges and cultural immersion rather than generic tours |
| 5 | **Komoot** | Expertise in outdoor navigation and route planning | Very niche (outdoors only) | Add cultural challenges with a social community |
| 6 | **Mapstr** | Save and share favorite places easily | More like a utility app (maps), lacks engagement, no gamification | Build on map sharing, but with interactive quests, culture and competition |


### Key Insights

#### Is there demand?  
Yes. Market trends indicate that travellers increasingly seek experiences over mere sightseeing. Platforms that are interactive and community-driven are especially popular among younger travellers.[[2]](#2)[[3]](#3)[[4]](#4)

#### What’s missing in current solutions?  
- Most travel apps focus on either utility (planning, booking) or authenticity (guided tours).  
- Few apps combine an interactive, culturally immersive experience with community building.  
- Existing solutions often lack interactivity, offline usability, or gamified side quests.  

#### How TravelGo! fills that gap  
- Integrates interactive, culturally immersive experiences with community engagement into a single platform.  
- Enables users to complete side quests, join challenges, and earn rewards while exploring off-beat locations.  
- Promotes social discovery by connecting travellers nearby.  
- Built with an offline-first architecture, considering real traveller needs such as spotty internet and battery constraints.


## Stakeholders

### Primary Stakeholders

- Tourists
  - main users of the platform
  - engage in competitive games, meet like-minded individuals and be interested in cultural enrichment
- Attraction Sites
  -  higher footfalls and visitor engagement resulting in an increase in ticket sales
-  Local Businesses
   -  advertisements and partnerships will gain more exposure, eliciting profits
   -  support special offers and discounts

### Secondary Stakeholders

- Government and Tourism Boards
  - boost in tourism while ensuring compliance of the local laws
  - control the digital platforms, tourism, and safeguarding the cultural
- Local Communities
  -  cultural representatives who gain from more interactions and business from tourists
  -  might be worried about cultural sensitivity
-  Developers and Designers
   -  responsible for creating, maintaining and upgrading the platform
-  Investors and Sponsors
   -  support financially and expecting returns in the form of partnerships, advertisements, subscriptions, and even positive publicity
  
### Tertiary Stakeholders

- Travel Agencies and Tour Operators
  - competitors or can be potential partners
- Online Travel Communities and Influencers
  - increase online engagement and positive word of mouth through social media 

<br>

![Power / Interest Grid](/img/Power_Interest_Grid.png)
Figure 1: Power / Interest Grid

## Personas

Personas are defined as fictional representations of users aimed to represent the diverse range of individuals
interacting with a specific application. They are used in order to observe and simulate a user’s interaction
with the platform once completed. Ultimately, constructing different personas can help identify weak points
and edge cases within the platform. In our case, all personas are assumed wto be unfamiliar with any programming knowledge.

### Tourist

This persona represents a typical travel enthusiast, visiting different countries and attractions. Each tourist as a bucket-list with attractions they decide to visit for that country. Tourists interact with each other, with guides, obtain discounts and discover new attractions.

### Local Business Owner (Internal Sponsor)

Since the app features discounts for various restaurants or souvenir shops, this persona represents local shop-owners that wish to improve their business. They process the monetary fee through the platform and in return offer the tourists a discount, voucher or even a free souvenir. Furthermore, the are also considered local sponsors since they ultimately wish for publicity for their business.

### Travel Agent

This persona represents a travelling expert with extended knowledge about various attractions. They help clients plan, book, and customize trips by offering professional advice on destinations, accommodations, and experiences.

### (Potential) External Sponsor

A sponsor is typically a brand, or local business which seeks visibility for their product among any individuals. They want to attract and engage individuals through gamified experiences and offered promotions in exchange for brand exposure.

## Epics

In this section, we list the epics, along with the corresponding description. Each epic has its features, which
further contribute to the User Stories. <span style="color:red">TBA later when further developed</span>.

## Features

| Feature ID | Feature Description | Relates User Stories |
|-----------|------------|-------------|
| F1         | Maintain an individual user bucket-list of attractions.          |        |
| F2         | Display a map with available countries and available attractions in each country.       |        |
| F2         | Maintain a community chatroom for attraction discoveries and user interactions.       |        |
| F3         | Display pop-up ads.          |        |
| F4         | <span style="color:red">have easter eggs (maybe/somehow)</span>          |        |
| F5         | Allow for premium features. (Let the user know when there are discounts for accommodation)        |        |
| F6         | Keep track of the user's daily quiz score and their placement in the leaderboard. |        |
| F7         | Reward the top competitors of the leaderboard with discounts, vouchers or free souvenirs. |        |

## User Stories

A user story is a brief description of a feature that a persona requires in the system. Furthermore, the overall benefit of this feature for the system’s development is also presented.

| User Story ID | User Story | Relates Tags |
|--------------|------------|-------------|
| US1           | As a Tourist, I wish to be able to see information for each attraction. |          |
| US2           | As a Tourist, I wish to be able to answer cultural questions about an attraction to improve my knowledge and receive points for completing a quiz per attraction. |          |
| US3           | As a Tourist, I wish to be able to participate in a country's league for the ultimate traveling champion. |          |
| US4           | As a Tourist, I want to engage with other travellers through a community platform. |          |
| US5           | As a Tourist, I want to be able to suggest new attractions in a country and earn points if my suggestion is validated. |          |
| US6           | As a Tourist, I wish to be able mark attractions as visited and cross them from my bucket-list. |          |
| US7           | As a Tourist, I want the platform to create a traveling plan for me, which I then will be able to export the external map applications. |          |
| US8           | As a Tourist, I want the platform to suggest nice local and traditional restaurants and open-area places when I am nearby and attraction. |          |
| US9           | As a Tourist, I want to pay extra for this platform to suggest me available accommodations near my current attraction that are also not crowded. |          |
| US10           | As a Tourist, I want to pay extra to remove pop-up ads. |          |
| US11           | As a Local Business Owner, I want the platform to recommend my business through pop-up ads. |          |
| US12           | As a Local Business Owner and Sponsor, I want the platform to offer 5% discounts for all platform users to increase publicity. |          |
| US13           | As a Local Business Owner, I want the free earned souvenir to have a representative picture on the platform. |          |
| US14           | As a Local French Restaurant Owner, I want the platform to recommend my business at the end of the quizzes for traditional places. |          |
| US15           | As a Travel Agent, I want offer city tours through TravelGo, for my clients to play along and for me to stand out from standard booking platforms. |          |
| US16           | As a Travel Agent, I want the platform to highlight premium guided tours or special events in collaboration with my agency in order to promote my business. |          |
| US17           | As an External Sponsor, I wish to financially support the platform's development in exchange for exposure. |          |


## Use Cases

Use cases explain how a user works with a system to accomplish certain tasks or objectives. They
outline the steps needed to achieve a set objective and also help define system requirements, derived from
the user stories.

| Use Case ID | Use Case Description | Relates Requirements |
|--------------|------------|-------------|
| UC1          | Automatically display a map of available countries. |          |
| UC2          | Automatically display a map of available attractions for the selected country. |          |
| UC3          | Create a traveling plan for a given number of visiting days. |          |
| UC4          | Create a sharable link of the traveling plan. |          |
| UC5          | Allow users to cross-off visited attractions from the plan/bucket-list. |          |
| UC6          | Offer a selection of questions, weighted in points. The summed points increase the user's daily score for the leaderboard. |          |
| UC7          | Determine the user's reward based on their score. |          |
| UC8          | Display pop-up ads for internal and external sponsors. |          |
| UC9          | Display available discounts for internal and external sponsors. |          |
| UC10          | Process subscription fee for unlocking premium for the user's account. |          |
| UC11          | Process shop fee for earned souvenir by the user. |          |
| UC12          | Maintain a hidden gem list of attractions. |      |
| UC13          | List various restaurants or outdoors environments for nearby attractions. |          |
| UC14          | (In case of premium) display a list of available accommodations. |          |
| UC15          | (In case of premium) Remove pop-up ads and any sort of advertisement. |          |

## Requirements

Requirements are documented descriptions a software system's tasks that it can perform or qualities
it should possess to fulfill stakeholders’ needs. Furthermore, they also provide key steps for solving
the user stories.

## Challenges

**1. Data Privacy & Trust** : TravelGo collects personal data like name, location, travel history. Mishandling of this data will lead to legal problems and loss of trust from customers.

* Ambiguity sources:
    1. How much data should be collected?
    2. How to balance personalization with privacy?
    3. How to handle cross-border compliance?

* Architectural implications:
    1. Must implement data minimization by only collecting necessary data.
    2. Needs strong consent management.
    3. Secure data storage & transmission.
    4. Potential need for regional data hosting.

**2. Cultural Sensitivity & Representation** : TravelGo promotes cultural quests and hidden gems. But what one person calls a “hidden gem” may be a sacred site or sensitive local tradition. Misrepresentation could cause backlash or even legal issues.

* Ambiguity sources:
    1. Who decides what is “authentic” enough to feature? 
    2. How do you avoid cultural appropriation or trivialization ?

* Architectural implications:
    1. Content vetting workflows: TravelGo might need local validators or an approval pipeline for sensitive submissions.
    2. Metadata tagging for cultural content for example, sensitive, sacred or family-friendly, requires flexible data models.
    3. May need regional customisation.

**3. Technical Constraints** : Travellers often have unreliable connectivity. But TravelGo’s core features like locating pins, chat and quests may depend on online services.

* Ambiguity sources:
    1. Which features should work offline? 
    2. How much data caching is feasible on a device without killing storage and battery?

* Architectural implications:
    1. May requires offline-first design.
    2. GPS tracking without internet would depend on OS support and API of offline maps.

**4. Community Moderation & Safety** : TravelGo’s chatrooms and commenting features are central to the social experience, but community spaces online are magnets for spam, harassment, scams, or inappropriate content.

* Ambiguity sources:
    1. Should moderation be automated using AI or keyword blocking, or human-led by moderators?
    2. How do you enforce rules across different cultures and languages?
    3. Should moderation be centralized or distributed?

* Architectural implications:
    1. Need for scalable content moderation pipelines.
    2. Storage and processing of flagged content would introduce compliance and legal liability.
    3. Balancing low latency (real-time chat) with content filtering can be technically tricky.

**5. Ecosystem Dependencies** : TravelGo will make use of third party APIs for functionalities like the map or login.

* Ambiguity sources:
    1. What happens if a provider changes pricing or kills an API?
    2. What if services are unavailable in some regions?
    3. Should you design for multi-provider fallback or lock-in with one provider?

* Architectural implications:
    1. Need abstraction layers and not hardcode to any single API.
    2. Consider vendor diversity.
    3. Monitor latency and reliability across providers.

## Wardley Map
The Wardley map for TravelGo highlights how the platform combines innovative, custom feautures with standardized, commodity services.
![WardleyMap](/img/WardleyMap.png)
<p style="text-align:center;">Figure 2 : Wardley map</p>

**Genesis** : This space contains novel, experimental features like side quests, cultural quizes and souvenir based rewards which are not yet mainstream in the travel tech domain. They provide differentiation, but also present a high risk of adoption and design.
**Custom Built**: Features like leaderboards and points system are placed here. While interactive platforms are popluar in other domains like fitness and education, applying it specifically to cultural travel remains relatively bespoke. These features distinguish TravelGo from commodity travel apps but are less risky than Genesis elements.
**Product Stage**: More well known features such as community chatrooms and posting comments fall under this category. These are standard capabilities available in many social or booking apps, but TravelGo customizes them for cultural travel contexts. They are visible to users but do not offer radical innovation.
**Commodity Stage**: Underlying infrastructure such as digital maps, location pinning, user accounts and APIs are considered commodity. They are invisible to end-users and widely available through third-party providers like Google Maps. TravelGo does not attempt to innovate here but instead rely on stable, low-cost services.
## Scenarios

<!--
Text here
-->

## Quality Attributes

<!--
Text here
-->

## System Context Diagram

<!--
Text here
-->

## Roadmap

![Roadmap](/img/Roadmap.png)
Figure 3: Roadmap

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
 
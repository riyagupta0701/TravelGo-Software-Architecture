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
We want to create an interactive digital platform that makes travelling easier and more fun for both group and solo travellers across various countries: TravelGo. Central to the platform is a map with all of the tourist attractions, including hidden spots. The platform aims to enrich cultural engagement with competitive games (for example quiz competitions) with a reward system through leaderboards. To make this competition fun for both inexperienced and experienced travellers, the platform uses a rating system with leagues. Users can aditionally earn points by going to an attraction and thus ticking it off their bucket list. These points can be used to for example get a discount on entry fees or to get an exclusive souvenir.

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
Since many travelling apps have been created ([Existing Solutions](#existing-solutions)), TravelGo does not have a lot of risks. There is a lot of reliable knowledge available. 

The main risks are the following:
- Correct information: Travelgo depends on information supplied by tourists and organizations. Since the platform will be available in multiple countries, it is difficult to examine all of the information.
- Privacy: TravelGo has access to the location and personal information of its users.
- External dependencies: TravelGo makes use of open source software.


## Market Research

## 1. Project Overview

TravelGo is an interactive travel companion platform that combines cultural immersion, social networking, and fun challenges to turn every trip into an adventure.

---

## 2. Target Audience

- **Backpackers / Solo travellers** who are seeking to be part of a community and want to find off-beat ideas.  
- **Young professionals / Digital nomads** who are looking for meaningful cultural immersion, not just sightseeing.  
- **Adventure seekers**, motivated by challenges, exploration, competition.  
- **Families or groups** looking for activities / side-quests which everyone can enjoy.  

---

## 3. Competitor Analysis

| Sr No. | Competitor | Strengths | Weaknesses | Opportunity for us |
|--------|------------|-----------|------------|---------------------|
| 1 | **TripRanger** | Gamifies travel, fun challenges | Limited user base, not mainstream, focus mostly on gamification rather than deep cultural immersion | We can combine interactivity and cultural depth, making it more meaningful |
| 2 | **Polarsteps** | Very popular, creates a visual travel journal, great for reliving your travel experiences. Helps share trips with friends and family | Mostly passive (recording, not interacting); limited social engagement beyond sharing | We add interactivity, side quests, community building |
| 3 | **Withlocals** | Popular; focused on authentic cultural experiences by connecting with locals/guides | Paid/expensive; depends heavily on guide availability; no gamification or community | Make authentic culture accessible and community driven |
| 4 | **Viator** | Huge catalog of tours & activities | Overly commercial and not personalized,lacks interactive features | Focus on personalized, fun challenges and cultural immersion rather than generic tours |
| 5 | **Komoot** | Expertise in outdoor navigation and route planning | Very niche (outdoors only) | Add cultural challenges with a social community |
| 6 | **Mapstr** | Save and share favorite places easily | More like a utility app (maps), lacks engagement, no gamification | Build on map sharing, but with interactive quests, culture and competition |

---

## 4. Key Insights

### Is there demand?  
Yes. Market trends indicate that travellers increasingly seek experiences over mere sightseeing. Platforms that are interactive and community-driven are especially popular among younger travellers.[^1][^2][^3]  

### What’s missing in current solutions?  
- Most travel apps focus on either utility (planning, booking) or authenticity (guided tours).  
- Few apps combine an interactive, culturally immersive experience with community building.  
- Existing solutions often lack interactivity, offline usability, or gamified side quests.  

### How TravelGo! fills that gap  
- Integrates interactive, culturally immersive experiences with community engagement into a single platform.  
- Enables users to complete side quests, join challenges, and earn rewards while exploring off-beat locations.  
- Promotes social discovery by connecting travellers nearby.  
- Built with an offline-first architecture, considering real traveller needs such as spotty internet and battery constraints.  

[^1]: ResearchGate, 2018. [Millennials and Gamification - A Model Proposal for Gamification Application in Tourism Destination](https://www.researchgate.net/publication/323457721_Millennials_and_Gamification_-_A_Model_Proposal_for_Gamification_Application_in_Tourism_Destination)  
[^2]: Atlys.com, 2025. [Gen Z Travel Trends](https://www.atlys.com/blog/gen-z-travel-trends)  
[^3]: CNBC, 2023. [Millennials are turning 40 and they’re changing travel as we know it](https://www.cnbc.com/2023/03/27/millennials-are-turning-40-and-theyre-changing-travel-as-we-know-it.html)
 

---


## Stakeholders

### Primary Stakeholders

- Tourists
  - main users of the platform
  - engage in competitive games, meet like-minded individuals and be interested in cultural enrichment
- Attraction Sites
  -  higher footfalls and visitor engagement resulting in an increase in ticketsales
-  Local Businesses
   -  advertisments and partnerships will gain more exposure, eliciting profits
   -  support special offers and discounts

### Secondary Stakeholders

- Goverment and Tourism Boards
  - boost in tourism while ensuring compliance of the local laws
  - control the digital platoforms, tourism, and safeguarding the cultural
- Local Communities
  -  cultural representatives who gain from more interactions and business from tourists
  -  might be worried about cultural sensitivity
-  Developers and Designers
   -  responsible for creating, maintaining and upgrading the platform
-  Investors and Sponsors
   -  support financially and expecting returns in the form of partnerships, advertisments, subscriptions, and even positive publicity
  
### Tertiary Stakeholders

- Travel Agencies and Tour Operators
  - competitors or can be potentail partners
- Online Travel Communities and Influencers
  - increase online engagement and positive word of mouth through social media 

<br>

![Power / Interest Grid](/img/Power_Interest_Grid.png)
Figure 1: Power / Interest Grid

## Use Cases and Features

<!--- 
Text here
-->

## Bibliography
<a id="1">[1]</a>
Bedjeti, Adriatik; Lago, Patricia; Lewis, Grace A.; De Boer, Remco D.; Hilliard, Rich (1968).
*Modeling Context with an Architecture Viewpoint*.
IEEE International Conference on Software Architecture (ICSA).

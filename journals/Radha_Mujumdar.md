## Week 1
Our group was formed on 2nd September. Soon after, I met the team for about an hour to get to know each other and discuss potential systems we could choose. On Thursday, 4th September, we finalized our system, "TravelGo!", after two meetings and extensive brainstorming. We initially considered domains like finance and disaster management, but evaluating feasibility and scope, we decided to explore other areas such as travel, which led to the idea of TravelGo.
## Week 2
On Monday, 8th September, we scheduled a meeting with the TA to discuss our system idea and the potential steps moving forward. After the meeting, the team met to divide tasks for the week. I was assigned the market research. On Tuesday, we collaborated in the library for about two hours to prepare the project plan, which was due on 15th September. Over the next few days, I focused on the market research section, analyzing potential competitors and their approaches.

## Week 3
- Had a team meeting on tuesday after the lecture on Wednesday from 3:30pm to 5:15pm where we worked on the following things 
    1. Reviewed work done until now on the report
    2. Discussed future steps and created the roadmap
    3. Designated tasks for week 3
    4. Brainstorming regarding POC
- Thursday and Friday, I then worked on the wardley map and challenges section for the report as discussed in the team meeting. Researched a bit about wardley maps and how can I create one for our system. Brainstormed on possible challenges and sources of ambiguity our system could face.
- Joined a team meeting online on Saturday from 7pm to 10pm. We went through the report together and gave feedback on each other's sections. Also, looked at the flow of the report and came up with a better, new structure for the same.
- Also implemented the suggested changes during the meeting, corrected a few things in the wardley map and added some info in the same section. Also removed the problem overview and target audience section as it was redundant and overlapped with other sections.

## Week 4
- On Monday, we had an online meeting to prepare for the peer to peer feedback session. We made a presentation and divided the parts for the presentation
- On Wednesday from 4 to 5 pm, we had our peer to peer feedback meeting along with the TA. We recieved some feedback from the other team with regards to our market research, stakeholders, quality attributes. We also gave the other team some feedback about their revenue stream 
- On Friday, during lecture we met with the professor to ask if he had any suggestions and thoughts aboit our report. He suggested to make the report more concise and avoid using generic info
- During the weekend, we had an online meeting again to discuss the feedback and make the refinement presentation. I worked on implementing the feedback and making the necessary changes. I also plan to study more about different architectural styles to reconsider the quality attributes and their tradeoffs as suggested by the other team.

## Week 5
- On Tuesday, 30th September, we met on google meet to discuss architectural styles and also reconsider our quality attributes. I read up on the sample report provided on brightspace. We divided different architectural styles amongst ourselves to explore and research to see which ones would fit our system the best. I looked up microservices one.
- On Wednesday, we had a team meeting at Aula between 4 to 6pm. We presented the designated architectural design to each other. After brainstorming for quite some time, we decided to go with the microservices architectural design. We then decided to look up different patterns under microservices. I researched about different patterns.
- On Friday, we had an online google meet to discuss and finalise our design pattern.  We decided to go with microservices using event driven comminication.  We also made a presentation for the TA meeting.
-I worked on my sections in the report on the weekend and explore ideas on how we will implement the poc.

## Week 6
- On Tuesday, we had a feedback meeting with the TA. He provided us with some valuable insights. Overall, he was quite happy with our progress. But he strongly advised us to look into kafka, as it would especially help us with the event driven architecture. We took notes about what I needed to improve upon and divided the tasks
- I added the connecting sentences to the wardley map for better flow and connection
- Then over the next few days, I looked into locust for proving the scalability quality attribute for the system. I plan to implement that in the following days as docker thing is done by Diana.
- Over the weekend, I researched about cloud scalability and how travelgo can make use of cloud infrastructure. I found that travelgo could really benefit from cloud infra and there are some good options out there in the market, but some sensetive information should be made hybrid. I added the discussion about cloud section in the report.
- Updated the roadmap and fixed the numbering in the report and for the bibliography.

## Week 7
- This week, I worked on proving the system's scalability. I researched possible options for the same, and finally decided on using locust as it was easier to implement than Jmeter or Gatling.
- We had a team meeting on Thursday in the campus where we discussed our progress and the next steps, what was remaining and what needed to be updated. 
- For the experminet, I coded the necessary files, and when I implemented it, I observed that there was no even distribution of the requests across service replicas, so I realised that a load balancer must be added to distribute the requests evenly. I used nginx for the same due to its easier integration.
- I observed that the response time decreased even though number of users increased as I implemented scaling and created replicas of chat service.
- I added my experiment section in the report about what was the aim of the experiment and what results were observed after it. 
- While reviewing the rubrics, I realized the open-source section lacked discussion on the components used in our architecture. I communicated this to the team and added NGINX and Locust to the section, justifying why they were the best fit for our system.
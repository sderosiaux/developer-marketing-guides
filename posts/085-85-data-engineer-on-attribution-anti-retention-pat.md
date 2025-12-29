---
number: 85
title: "Data engineer on attribution, anti-retention patterns, and an ad breakdowns gallery"
slug: "85-data-engineer-on-attribution-anti-retention-patterns-and-an-ad-breakdowns-gallery"
url: "https://newslepear.beehiiv.com/p/85-data-engineer-on-attribution-anti-retention-patterns-and-an-ad-breakdowns-gallery"
date: "October 13, 2024"
---



# Developer marketing insights
### 1. Dev tool ad breakdowns gallery
[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c6d6a849-cacc-49bd-a533-395cc8321892/Zach_Example_Gallery.png)](https://picturesque-macrame-365.notion.site/Ad-breakdowns-89a4ab4339784b58bb13c15793b7d326)
[See Zach’s gallery](https://picturesque-macrame-365.notion.site/Ad-breakdowns-89a4ab4339784b58bb13c15793b7d326)
Zachary Short has compiled a fantastic [gallery of (mostly dev tool) ad breakdowns. ](https://picturesque-macrame-365.notion.site/Ad-breakdowns-89a4ab4339784b58bb13c15793b7d326)
They are organized by the ad style and campaign focus. Great stuff if you are looking for inspiration when it comes to ad creatives. 
Also, give [Zach](https://www.linkedin.com/in/zachary-f-short/) a follow if you want to stay in the loop for ad breakdowns and/or really funny rants ;)
### 2. Data engineer turned marketer on attribution 
[Sarah Krasnik Bedell ](https://www.linkedin.com/in/sarahkrasnikbedell/)is a Data Engineer turned Director of growth marketing and put together an awesome article and video on marketing attribution. 
[https://sarahsnewsletter.substack.com/p/marketing-attribution-a-guided-map](https://sarahsnewsletter.substack.com/p/marketing-attribution-a-guided-map)
My takeaways:
  * (First-party cookie) **ad-blocking is perhaps not as common**. For Prefect the % of devs who signed up and used ad-blockers sits consistently at around 10%. 
  * It is likely **way higher for third-party cookies** but you can use a reverse proxy and first track things with first-party cookies (your server) and then send the cookie to the third-party. 
  To assess how important** doing the reverse proxy is for you compare signups by month as tracked in your database vs signups tracked in your analytics tool. 
  * Consider the **ranked touch model**(vs first/last touch). You rank which channels/programs should be attributed if multiple touchpoints occur. Like you read a blog (channel 1) and click on a social ad (channel 2). If I rank paid social over Blog I’d attribute that to paid social. 
  * When reporting, **each chart should answer a question you care about**. If you look at a chart, say cool, and do nothing, it is likely not a good chart. Examples of good is knowing which channels bring the most top-of-funnel awareness, or where the most active users come from. 
  Test out the implementation**. Look at the analytics tool and your website side-by-side and see that what you do on the website gets properly attributed to the real-time dashboard of your tool. Most of the weird-looking dashboards are the result of a bug, not actual behavior. 

[Read the full article ->](https://sarahsnewsletter.substack.com/p/marketing-attribution-a-guided-map)
### 3. Anti-retention patterns
[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2ad72db2-1f43-4298-aaac-ec8c548cfe1f/image.png)](https://open.spotify.com/episode/2PNnZhL8agfBaWa2lfYmXJ?si=3e0c012f76d346d4&utm_source=newslepear.beehiiv.com&utm_medium=referral&utm_campaign=85-data-engineer-on-attribution-anti-retention-patterns-and-an-ad-breakdowns-gallery)
[Listen to episode](https://open.spotify.com/episode/2PNnZhL8agfBaWa2lfYmXJ?si=3e0c012f76d346d4&utm_source=newslepear.beehiiv.com&utm_medium=referral&utm_campaign=85-data-engineer-on-attribution-anti-retention-patterns-and-an-ad-breakdowns-gallery)
This is an interesting concept coming from [Gonto](https://www.linkedin.com/in/mgonto/) he discovered while working on Auth0 adoption/retention.
**Anti-retention adoption patterns** :
  * You have a product that has many features, many levels of value extracted
  * Adopting certain features too early may actually lead to lower retention later
  * You should **compare users who retained and haven’t** after a mid/longer term and **see which features they adopt** and when. Plot out feature adoption by time for those two groups. 
  * They did that with multifactor auth at auth0 and it turned out that “blocking” it, or giving devs a big fat info box saying that this is not recommended to implement yet, pushed the retention up. 

[Listen to the full episode ->](https://open.spotify.com/episode/2PNnZhL8agfBaWa2lfYmXJ?si=3e0c012f76d346d4&utm_source=newslepear.beehiiv.com&utm_medium=referral&utm_campaign=85-data-engineer-on-attribution-anti-retention-patterns-and-an-ad-breakdowns-gallery)

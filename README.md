# CLARE

CLARE - Crawler for Link Analysis and Reporting

This has been featured in my article in linkedin - Subscribe on LinkedIn https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7087824083161088002

It identifies broken links in the documents. It is assumed that the documents are hosted in some server accessible over HTTP. 

It has got 3 steps:
1. Access URL
2. Parse the html document, find all hyper-links
3. repeat step 1 for each link and note their http status.
4. publish report when all links have been traversed.

<img width="266" alt="Screenshot 2023-08-05 at 5 23 27 PM" src="https://github.com/RoyAmitabh/CLARE/assets/104931628/66a64640-2b89-4cc1-8cb3-d90083cdf22c">


Report should look like : 

Page: URL, percentage of broken links

https://www.example.com, 75% 

This repository contains files :

1. crawler - main.py
2. fastapi - sample_wiki.py. This is for hosting a sample document over localhost to test out the logic. This is optional for crawler.
3. how to host fastapi - howto.txt

   
This code does not intend to use robots.txt. It is for personal use. In case you need to let this crawler work over websites not owned by you, please utilise robots.txt file. I have another repository showing how to use robots.txt file while crawling. 

Also, the sample code expects no authentication for fetching the contents. If you intend to use it for a document that is behind auth layer, you must tweak it accordingly.

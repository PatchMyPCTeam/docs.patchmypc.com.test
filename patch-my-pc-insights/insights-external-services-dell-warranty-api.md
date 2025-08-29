# Insights External Services Dell Warranty API

_Applies to: Patch My PC Advanced Insights_

Advanced Insights (this is not relevant for Patch Insights) can access device warranty information from a variety of vendors. For access to Dell warranty information you will need an API key provided by Dell. The process to apply for a key is shown here.

First you will browse to [https://techdirect.dell.com](https://techdirect.dell.com/) and register or log in, you will need to be associated with your Dell Company account. Once all that is sorted you can select to go to the APIs section.

![](../_images/image%20%281293%29.png%20"Dell%20Tech%20API")

![](../_images/image%20%281289%29.png%20"Dell%20Tech%20Request%20API%20Key")

![](../_images/image%20%281562%29.png%20"Dell%20API%20Client%20ID")

![](../_images/image%20%281563%29.png%20"Dell%20API%20Client%20Secret")



{% hint style="info" %}
Advanced Insights makes a single API call for every 100 Dell clients when importing warranty information. To estimate the number of API calls you will require, we recommend specify 1% of the total Dell client device count.
{% endhint %}

Once you have successfully obtained your API key log into Advanced Insights and navigate to the Administration area. Go to Settings - External Services and check the "Is Enabled" and "Enable Warranty Caching" option.&#x20;

Enter the provided Dell warranty text for Client ID, Client Secret and click save all.

\*Please only enter in the text in-between the brackets for the API Client Secret.

![](../_images/image%20%281561%29.png%20"Example%20of%20Dell%20API%20Client%20ID%20and%20Client%20Secret")

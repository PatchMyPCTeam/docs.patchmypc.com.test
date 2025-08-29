# Insights External Services HP Warranty (Workforce Experience)

_Applies to: Patch My PC Advanced Insights_

Advanced Insights (this is not relevant for Patch Insights) can access device warranty information from a variety of vendors. For access to HP warranty information you will need to sign up to HP Workforce Experience, enroll all the HP devices you want to collect warranty data on and set up a developer account to access the warranty data.

{% hint style="danger" %}
You will need to be a HP Workforce Experience customer for this to work, please speak to your HP representative about becoming a customer.
{% endhint %}

## Developer account creation

First, we will create the developer account needed to interact with the HP Workforce Experience api.

### Initial setup

#### API Enrolment

{% hint style="info" %}
The url for the HP developer portal is [https://developers.hp.com/](https://developers.hp.com/)
{% endhint %}

First, you will need to create an account if you do not have one already. If you have a HPID for HP Workforce Experience, you can use this account.&#x20;

{% hint style="danger" %}
Once you have registered, you will need to request access to the HP Proactive Insights APIs tech group for your developer account. The group required is HP Proactive Insights and not HP Warranty API. We do not currently support the HP Warranty API at this time.&#x20;
{% endhint %}

### Creating credentials

{% hint style="info" %}
The link to generate api credentials is: [https://developers.hp.com/group/1275/manage-credentials/apis](https://developers.hp.com/group/1275/manage-credentials/apis)
{% endhint %}

Please visit the link above to open the credentials generation page. You will be show the following options below. Click Get Credentials in the HP Proactive Insights Analytics section.&#x20;

![](../_images/image%20%281937%29.png%20"Link%20location%20to%20create%20api%20credentials")

{% hint style="warning" %}
If the page has an error screen like shown below, HP have not enrolled your developer account in the HP Proactive Insights APIs tech group. Please contact HP again to have your account enrolled in the HP Proactive Insights API tech group.&#x20;
{% endhint %}

![This image showcases the Hp Proactive Insights API web page, with the error You do not have appropriate permissions (role) to access any of this Tech Groups published Apis](../_images/hp%20no%20api%20%281%29.png%20"HP%20enrolment%20error")

#### Credentials creation flow

![](../_images/image%20%281938%29.png%20"Credentials%20creation%20form")

You will need to provide the following information:

1. Credentials name: We recommend "Advanced Insight Warranty"
2. Description: We recommend "API Keys for Advanced Insight Warranty"
3. Developer Redirect Url: This will be used by HP to redirect when you log in. This needs to be your Advanced Insights in the following format _https://FQDN:PORT/app/main/view/warranty_. Example https://contoso.local:444/app/main/view/warranty
4. Client ID: Leave blank
5. Tick Read Checkbox

![](../_images/image%20%281940%29.png%20"Complete%20example%20of%20credentials%20creation")

Click create and you will be redirected back to the previous page.

#### Viewing app

![](../_images/image%20%281941%29.png%20"Green%20banner%20showing%20creation%20was%20successful")

Once you have been redirected, there will be a green success banner on top of the page. Please now click the "My API Credentials" link in the banner.&#x20;

![](../_images/image%20%281942%29.png%20"App%20listing%20with%20newly%20created%20app")

Now click on the newly created app by click the app name, this will load the app details page.

![](../_images/image%20%281944%29.png%20"App%20details%20page")

Here you will see information about the newly created app.&#x20;

We need to copy

1. The API ClientId
2. The API Secret (click "Show Secret" to get this entry)

{% hint style="warning" %}
It's a good idea to double check that the Redirect URL is correct. You can come back to this page if you receive a redirect URL error when trying to authenticate. You will also want to change the URL if your installation FQDN of Advanced Insights changes in the future.
{% endhint %}

### HP Settings in Advanced Insights

We now need to copy API ClientId and API Secret to Advanced Insights.&#x20;

1. Go to Administration -> Settings -> External Services
2. Based on the location of the HP Workforce Experience portal you used, select US or EU.&#x20;
3. Copy and paste the API Client ID into the Client ID input
4. Copy and paste the API Client Secret into the Client Secret input
5. Save settings.

![](../_images/image%20%281866%29.png%20"Settings%20page%20in%20Advanced%20Insights")



{% hint style="info" %}
The app client secret has an expiration date of one year from the date of creation. Please make a note of when this key will need to be rotated.
{% endhint %}

## Register for HP Workforce Experience

{% hint style="warning" %}
If you are already a HP Workforce Experience customer, you may not need to do the registration steps below but you will need access to the HP Workforce Experience Portal.



HP has two versions of HP Workforce Experience, one for US (and ASIA) customers and one for EU customers.&#x20;

You will need to sign up to the appropriate version based on your companies location.&#x20;

Mistakes here will cause issues in the future. Here are the access urls.

US portal: [https://admin.hp.com/](https://admin.hp.com/)

EU portal: [https://eu.admin.hp.com/](https://eu.admin.hp.com/)
{% endhint %}

![](../_images/image%20%281876%29.png%20"HP%20Workforce%20Experience%20welcome%20page")

![](../_images/image%20%281877%29.png%20"Sign%20up%20or%20login%20using%20either%20a%20Microsoft%20Account%20to%20or%20HPID%20account")

![](../_images/image%20%281879%29.png%20"Create%20HP%20Workforce%20Experience%20Account")

![](../_images/image%20%281880%29.png%20"Account%20creation%20dialog")

![](../_images/image%20%281882%29.png%20"Accepting%20the%20ToS")

## Using HP Workforce Experience

When you have registered and logged in, you will be greeted by the home experience of HP Workforce Experience. \
On the left hand side, you will need to click "Assets" to begin importing your HP devices into HP Workforce Experience.

![](../_images/image%20%281838%29.png%20"HP%20Workforce%20Experience%20homepage%20with%20assets%20link%20highlighted")

### Importing devices

HP Workforce Experience allows you to import your device using four different mechanisms. Currently **only Intune Import and Asset enrolment allow for warranty data collection**, manual and csv upload do not trigger warranty collection by design. To begin importing devices, please click the "Add" button in the top left of the page.

![](../_images/image%20%281840%29.png%20"Assets%20page%20with%20assets%20imported")

![](../_images/image%20%281841%29.png%20"Add%20button%20for%20device%20import")

### Intune import

To begin importing from Intune, please click the Intune Import button then click next.

![](../_images/image%20%281843%29.png%20"The%20import%20modal,%20please%20click%20Intune%20Import%20then%20next")

You will be now asked to provide your Intune Domain Name, this can be found by going to the Intune portal, clicking Tenant Administration on the left hand menu and copying the Tenant name from the Tenant Status page.&#x20;

![](../_images/image%20%281844%29.png%20"Location%20of%20tenant%20domain%20name,%20via%20Intune%20portal.")

![](../_images/image%20%281845%29.png%20"Adding%20our%20tenant%20domain%20name%20to%20HP.")

You will now be greeted by the Microsoft Login flow, please log in using your microsoft credenitals as normal. You will be then presented the list of permission HP requests to perform the Intune import.

{% hint style="warning" %}
All of the permissions requested by HP is for the HP Workforce Experience platform. They are not defined/requested by Patch My PC. Advanced Insights does not use or read any of your Intune data.
{% endhint %}

![](../_images/fixed.png%20"Permissions%20required%20by%20HP.")

Once you have accepted the permission, the connection to Intune will be completed by HP.&#x20;

You will now be asked if you wish to import Assets from Intune Groups, or to import all of your assets.

{% hint style="info" %}
We recommend you use the Group functionality, as this allows you to only provide HP the devices you wish to collect warranty information on. Only use full import if you really want every device in HP Workforce Experience as it is vendor agnostic and will collect all competing vendor devices.
{% endhint %}

We shall continue using Group import only.&#x20;

When you click on Import assets only from Intune groups, you will be presented with a full list of all your groups in Intune. You can filter out the groups you want to import and you can import multiple groups. Select the groups you want to import and click Import.&#x20;

![](../_images/image%20%281847%29.png%20"Filtered%20group%20for%20HP%20devices%20only")

Intune will now begin importing your selected devices. You will receive a notification on begin and completion of the import.&#x20;

![](../_images/image%20%281850%29.png%20"")

You can also check progress by navigating to the logs link on the left hand side.&#x20;

### Asset Enrolment

To enrol your device by Asset Enrolment, please use the following HP documentation to distribute the agent.

[Via SCCM](https://hp.service-now.com/workforceexperience?id=kb_article\&sysparm_article=KB0011362)

[Via Intune](https://hp.service-now.com/workforceexperience?id=kb_article\&sysparm_article=KB0011387)

{% hint style="success" %}
Once the devices are imported, HP Workforce Experience will begin collecting warranty information. This process can take some time, depending on how many devices you have imported.&#x20;
{% endhint %}

## Collecting Warranty

Collecting warranty in Advanced Insights works in the same way as the other providers, but you will need to log into HP on bulk caching.&#x20;

Navigate to the warranty dashboard.&#x20;

To begin, click the "Bulk Processing" statistic to begin re-caching warranty.

![](../_images/image%20%281868%29.png%20"Warranty%20dashboard")

You will be asked to log in to HP, click yes and Advanced Insights will go to HP to log in.&#x20;

![](../_images/image%20%281869%29.png%20"HP%20login%20warning")

{% hint style="danger" %}
If you receive a redirect url is incorrect error. Please go back to your developer app and check the redirect url provided.&#x20;
{% endhint %}

{% hint style="success" %}
Once you have logged in, HP will redirect you back to Advanced Insights and warranty will begin caching warranty data.
{% endhint %}

![](../_images/image%20%281836%29.png%20"HP%20Warranty%20data%20listed%20in%20Advanced%20Insights")

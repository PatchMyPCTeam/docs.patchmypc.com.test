# Cloud "Summary" Deployment tab

_Applies to: Patch My PC Cloud_

{% hint style="info" %}
**Note**

Reviewing the **Summary** tab is optional, but recommended.
{% endhint %}

The **Summary** tab of the Patch My PC (PMPC) Cloud deployment wizard provides a summary of the deployment so you can confirm that it is configured correctly before you create it.

![&#x22;Summary&#x22; tab](/_images/image-%282391%29.png-"&#x22;Summary&#x22;-tab" "&#x22;Summary&#x22; tab")

Review the summary of the deployment shown on the **Summary** page.\
\
If you are happy click **Deploy**.\
\
If you need to change something, click **< Prev** to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click **Deploy**.

![Clicking &#x22;Deploy&#x22;](/_images/image-%282392%29.png-"Clicking-&#x22;Deploy&#x22;" "Clicking &#x22;Deploy&#x22;")

{% hint style="info" %}
Note

If you have configured this deployment to use [Update Rings](../cloud-update-rings/), you will see the **Deployment Summary** screen, containing details on how you have configured the rings.

!["Deployment Summary" shown if this deloyment is using Update Rings](/_images/image-%282291 "\"Deployment Summary\" shown if this deloyment is using Update Rings").png>)

See [Update Rings](../cloud-update-rings/) for more information.
{% endhint %}

The App Catalog is redisplayed along with the **Success - Created&#x20;**_**\<deployment\_name>**_ notification.

![](/_images/image-%282393%29.png-"" "")

{% hint style="warning" %}
**Important**

When a new version of software is released, it is automatically deployed using the settings of the existing deployment. The old version will be removed from the target user/device and replaced with the newer version.
{% endhint %}

{% hint style="info" %}
**Note**

By default, the installation logs for an app will be created in the following folder regardless of the installer file type:

`%ProgramData%\PatchMyPCInstallLogs`

The only exception is for EXE files, where the specified value for the **loggingSwitch** variable will be used if it is not null or empty.
{% endhint %}

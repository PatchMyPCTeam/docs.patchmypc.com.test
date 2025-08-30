---
description: Change the Advanced Insights SSL Certificate.
---

# Modify Insights SSL Certificate

_Applies to: Patch My PC Advanced and Patch Insights_

This section describes the steps required to change the SSL certificate used for an existing Advanced Insights deployment.

{% hint style="warning" %}
The ability to change the SSL certificate using the modify feature is supported in version 2.1.0 and later.
{% endhint %}

{% hint style="warning" %}
Review the SSL Certificate requirements here: [insights-ssl-certificate-configuration.md](../download-and-install-insights/insights-ssl-certificate-configuration.md "mention")
{% endhint %}

{% hint style="info" %}
In this example, we are changing the SSL certificate to a CNAME / Alias type as described here - [#cname-alias-certificate](../download-and-install-insights/insights-ssl-certificate-configuration.md#cname-alias-certificate "mention")\
\
If you want to change the SSL certificate to a server host name only type, select the appropriate certificate and then click **'Next'.** Configuring a server host name type URL described here **-** [#standard-server-host-name-certificate](../download-and-install-insights/insights-ssl-certificate-configuration.md#standard-server-host-name-certificate "mention")
{% endhint %}

In the configuration modification page, select the checkbox for 'SSL Certificate' then click 'Change Certificate':

![](/_images/vmconnect_KN0zxDuJp8.png-"" "")

Use the drop down list to select the SSL certificate which represents the CNAME / Alias you wish to use.

![](/_images/image-%281654%29.png-"Certificate-selection-dialog" "")

With the appropriate SSL certificate selected, click **'Set CNAME / Alias'**

![](/_images/image-%281655%29.png-"Certificate-selection-dialog" "")

In the set CNAME / Alias dialog page, the dialog will be prepopulated with a value for the CNAME / Alias based upon the selected certificated.

Modify the prepopulated URL value if required.

Click **'Set CNAME / Alias'**

![](/_images/Alias-dialog" "")

Click **'Next'**

![](/_images/Alias-set-confirmed" "")

Click **'Install'**

![](/_images/vmconnect_KN0zxDuJp8-%282%29.png-"Certificate-Modification-option-dialog" "")

The installer will make the required configuration changes and display a summary once complete.

Click **'Finish'**

![](/_images/image-%281658%29.png-"Certificate-modification-completion" "")

New Advanced Insights URL

![](/_images/vmconnect_hyyumsMyOf.png-"New-Advanced-Insights-URL" "")

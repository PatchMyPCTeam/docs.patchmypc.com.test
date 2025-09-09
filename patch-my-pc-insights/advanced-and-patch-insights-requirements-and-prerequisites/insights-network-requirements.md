---
description: Details of port and external site requirements and supported browsers.
---

# Insights  Network Requirements

_Applies to: Patch My PC Advanced and Patch Insights_

### Network Ports <a href="#network-ports" id="network-ports"></a>

Advanced Insights use the following ports, and the installer will automatically create Windows firewall exceptions for these ports.

* Advanced Insights Frontend - <strong>tcp/443</strong> (or whatever you have customised this to in the installer)
* Advanced Insights API - <strong>tcp/44301</strong> (cannot be changed)

<blockquote class="wp-block-quote">
<p>Both ports (443/custom frontend port and 44301) need to allowed through your firewall or network filtering software for internal network access to the application. If you want Advanced Insights to be accessed by multiple remote devices, please follow the appropriate procedure to unblock these two ports on your network.</p>
<p>You will more than likely see either no login screen, or an error message stating "Unable to Connect to the API Server" if either of these ports are blocked. &#x20;</p>
</blockquote>

<strong>*

### RPC Traffic (<mark style="color:yellow;">If using remote server</mark>)

If you are using a remote Advanced Insights server there are these requirements to use any console actions or features:

* The Remote Procedure Call (RPC) service must be running
* Firewall must allow RPC Traffic to your ConfigMgr Provider (TCP ports: </strong>135<strong>, </strong>RPC dynamic ports (49152–65535)<strong>

Details on how to configure a firewall rule to allow this traffic can be found here: [https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)&#x20;

</strong>*

### Internet Access Requirements

The Advanced Insights server needs access to various domains and APIs to function fully.&#x20;

#### Essential Addresses

* <strong>api.patchmypc.com:443</strong>
  * Reason: For licensing
* <strong>learn.microsoft.com:443</strong>
  * Reason: For ConfigMgr, Windows, and Office 365 release and support statements

<blockquote class="wp-block-quote">
<p>Important: To activate and use Advanced Insights, you must permit outbound access for api.patchmypc.com:443</p>
</blockquote>

#### Recommended Addresses

* <strong>api.msrc.microsoft.com:443</strong>
  * Reason: The Threat Analytics dashboard uses data from this external API
* <strong>services.nvd.nist.gov:443</strong>
  * Reason: The Threat Analytics dashboard uses data from this external API for PMPC CVE data
* <strong>access.redhat.com:443</strong>
  * Reason: The Threat Analytics dashboard uses data from this external API for PMPC CVE data
* <strong>getcallisto.io:443</strong>
  * Reason: The Advanced Insights inventory extensions
* <strong>api.callisto.co:443</strong>
  * Reason: The Advanced Insights Threat Analytics API&#x20;
* <strong>supportapi.lenovo.com:443</strong>
  * Reason: To retrieve data from the Lenovo warranty service
* <strong>apigtwb2c.us.dell.com:443</strong>
  * Reason: To retrieve data from the Dell warranty service
* <strong>support.dynabook.com:443</strong>
  * Reason: To retrieve data from the Toshiba warranty service
* <strong>eu.daas.api.hp.com:443</strong> or <strong>daas.api.hp.com:433</strong> (depending on your region)
  * Reason: To retrieve data from the HP Workforce Experience warranty service

<blockquote class="wp-block-quote">
<p>To use these features of Advanced Insights, you will need outbound access to the above addresses.</p>
</blockquote>

***

### Browsers

<blockquote class="wp-block-quote">
<p>We do not support Internet Explorer for Advanced Insights. Please use Firefox, Edge, Chrome or any other modern browser to access Advanced Insights.</p>
</blockquote>
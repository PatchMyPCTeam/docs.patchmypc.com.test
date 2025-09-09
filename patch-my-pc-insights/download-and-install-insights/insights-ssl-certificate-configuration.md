---
description: Advanced Insights SSL Certificate configuration.
---

# Insights SSL Certificate Configuration

_Applies to: Patch My PC Advanced and Patch Insights_

Advanced Insights requires a valid SSL certificate to bind to the application websites and supports the following types:

* Server host (FQDN) standard certificate.
* Wildcard certificate.
* Custom CNAME / Alias certificate.
* Self-signed certificate.

<blockquote class="wp-block-quote">
<p>Ensure the SSL certificate requirements are reviewed here: [insights-certificate-requirements.md](../advanced-and-patch-insights-requirements-and-prerequisites/insights-certificate-requirements.md "mention")</p>
</blockquote>

### Certificate configuration scenarios

* <strong>Scenario 1 - Server Host name certificate.</strong>
  * For Advanced Insights URL deployment using <strong>server host name</strong> (e.g. _https://server01.contoso.local_) follow steps described in section:[#standard-server-host-name-certificate](insights-ssl-certificate-configuration.md#standard-server-host-name-certificate "mention")
* <strong>Scenario 2 - Wildcard certificate.</strong>
  * For custom Advanced Insights URL deployment using a <strong>wildcard certificate</strong> (e.g. \*.contoso.local) follow steps described in section: [#wildcard-certificate](insights-ssl-certificate-configuration.md#wildcard-certificate "mention")
* <strong>Scenario 3 - CNAME / Alias certificate.</strong>
  * For custom Advanced Insights URL deployment using a <strong>CNAME / Alias,</strong> (e.g. _https://AdvancedInsights.contoso.local_) follow steps described in section: [#cname-alias-certificate](insights-ssl-certificate-configuration.md#cname-alias-certificate "mention")
* <strong>Scenario 4 - Self-signed certificate.</strong>
  * For Advanced Insights URL deployment using a <strong>Self-signed</strong> certificate follow steps described in section: [#self-signed-certificate](insights-ssl-certificate-configuration.md#self-signed-certificate "mention")



## Standard Server host name certificate

Select the certificate which represents the server host name (FQDN).

![](/_images/image-(1297).png "Certificate selection")

Once selected, no further certificate configuration is required.

Click Next to proceed to the [insights-sqlite-database.md](insights-sqlite-database.md "mention") page.

## Wildcard certificate

Select the certificate which represents the wildcard certificate.

![](/_images/image-(1298).png "Wildcard certificate selection")

Click the <strong>'Set CNAME / Alias'</strong> button.

In the CNAME / Alias configuration page, the installer will automatically pre-populate the domain wildcard property from the selected certificate.

![](/_images/image-(1300).png "Wildcard CNAME / Alias URL configuration")

The CNAME / Alias property value box will need to be updated with a chosen CNAME / Alias prefix. For example:

_<strong>'AdvancedInsights.corp.contoso.local'</strong>_

Then click <strong>'Set CNAME - Alias'</strong>.

![](/_images/image-(1302).png "Setting CNAME / Alias property value")

Click Next to proceed to the [insights-sqlite-database.md](insights-sqlite-database.md "mention") page.

![](/_images/image-(1303).png "Set CNAME / Alias confirmation")

<blockquote class="wp-block-quote">
<p>When using a wildcard certificate, if no CNAME / Alias is set using the CNAME / Alias configuration page, the installer will automatically default to setting the Advanced Insights URL to the server host name FQDN.\</p>
<p>\</p>
<p>Example:&#x20;</p>
<p>_https://server01.corp.contoso.local_</p>
</blockquote>

## CNAME / Alias certificate

Select the certificate which represents the CNAME / Alias certificate.

![](/_images/image-(1299).png "CNAME / Alias certificate selection")

Click the <strong>'Set CNAME / Alias'</strong> button.

In the CNAME / Alias configuration page, the installer will automatically pre-populate the CNAME / Alias property based on the available SAN entries from the selected certificate.

In this example, the selected certificate has one SAN entry which has been automatically pre-populated:

![](/_images/image-(1304).png "CNAME / Alias URL configuration")

Confirm the CNAME / Alias configuration by clicking the <strong>'Set CNAME / Alias'</strong> button.

![](/_images/image-(1305).png "Setting CNAME / Alias property value")

Click Next to proceed to the [insights-sqlite-database.md](insights-sqlite-database.md "mention") page.

## Self-signed certificate

To deploy Advanced Insights using a self-signed certificate, on the certificate selection page, click the <strong>'Create Self -Signed Cert'</strong> button:

![](/_images/image-(1022).png "Create self-signed certificate")

The installer will then automatically proceed to the [insights-sqlite-database.md](insights-sqlite-database.md "mention") dialog page.
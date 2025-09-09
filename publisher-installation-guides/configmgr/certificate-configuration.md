---
description: >-
  When working with a Configuration Manager or WSUS implementation, proper
  certificate configuration is crucial.  Microsoft requires all updates to be
  signed.
---

# Certificate Configuration

_Applies to: On-premises Publisher_

## Certificates

When working with a Configuration Manager or WSUS implementation, proper certificate configuration is crucial. One way <strong>Microsoft helps ensure an update is considered secure and from a trusted source</strong> is through the utilization of a code signing certificate. This requirement means all custom updates must be code signed before injection into WSUS. We provide three different ways to configure the certificate.&#x20;

In most organizations, <strong>allowing Configuration Manager to manage the certificate</strong> is acceptable and the easiest option. There may be external requirements that prevent the usage of self-signed certificates. To read our in-depth guide on certificates click the link below.

{% embed url="https://patchmypc.com/wsus-signing-certificate-options-for-third-party-updates-in-configuration-manager" %}

If a self-signed certificate managed by Configuration Manager, is acceptable for your organization complete the steps below.

## Self Signed - Configuration Manager Managed

If you are running SCCM 1806 or newer, you can enable the option for “Configuration Manager manages the certificate” in the Software Update Point configuration. To configure this setting complete the following steps.

Begin by opening the configuration manager console and then

1. Select <strong>Administration</strong>
2. Expand Site Configuration and select <strong>sites</strong>
3. Select your topmost Site (If you have a CAS, select the CAS) - <strong>Right click the site</strong>
4. Select <strong>Configure Site Components</strong>
5. Select <strong>Software Update Point</strong> from the fly-out.

![](/_images/image-(1194).png>)

This will open up the software update point management component tab. From this window complete the following steps if not already done.

1. Select the <strong>Third Party Updates</strong> Tab
2. Validate <strong>Enable third-party software updates</strong> is checked.&#x20;
3. Validate <strong>Configuration Manager manages the certificate</strong> option is selected.
4. Select <strong>Apply</strong>

![Enable Third  Party Updates and allow Configuration Manager to manage the certificate.](/_images/image (1112).png>)

<blockquote class="wp-block-quote">
<p>If your <a href="https://docs.microsoft.com/en-us/mem/configmgr/sum/get-started/install-a-software-update-point">software update point </a><strong>site system is remote from the site server</strong>, SSL needs to be <a href="https://docs.microsoft.com/en-us/mem/configmgr/sum/get-started/software-update-point-ssl">configured on WSUS</a> for the option _<strong>Configuration Manager manages the certificate to work</strong>_. If SSL is not configured in this scenario, you will need to use an alternative method described here <a href="https://patchmypc.com/how-to-deploy-the-wsus-signing-certificate-for-third-party-software-updates">create and deploy the WSUS signing certificate</a>.</p>
<p><strong>Note</strong>: Switching WSUS to require SSL does not require client authentication certificates on all devices, it only requires a SSL certificate on the WSUS server that <strong>clients trust</strong>.</p>
</blockquote>

Once enabled, SCCM will automatically generate the signing certificate <strong>during the next software update point sync</strong>. You can force a software update point sync at any time. To force a software update point sync, complete the following steps.&#x20;

1. Browse to <strong>Software Library</strong>
2. Expand  and <strong>Software Updates</strong> > <strong>Right-click All Software Updates</strong>
3. Select <strong>Synchronize Software Updates</strong>
4. Hit <strong>OK</strong> on the pop-up message.

![Synchronize Software Updates to generate a new certificate](/_images/image (1157).png>)

If you want to watch, and confirm the certificate is properly created, you can open the <strong>wsyncmgr.log</strong> this log is located in <strong>%ConfigMgr Install Directory%\Logs\wysnmgr.log.</strong> Alternatively, you can click the button displayed below in the Publisher General Tab.&#x20;

![](/_images/image-(1172).png>)

<blockquote class="wp-block-quote">
<p>The <strong>Open wsyncmgr.log</strong> will only show up if the Publisher is installed on the site server. This may not be the case if your top-level software update point is not the site server.</p>
</blockquote>

With the log file open you'll want to watch for the entry stating the certificate was inserted. This indicates the certificate has been generated and is ready to be used.&#x20;

![](/_images/image-(1222).png>)

You can ascertain if the certificate exists and is ready for use by clicking the <strong>Show Certificate</strong> button in the publisher.

![Here the certificate exists but has not been checked, select Show Certificate](/_images/image (1195).png>)

![Here is the information around the generated certificate](/_images/image (1078).png>)

![Note how the checkbox is now green. You are ready to start publishing updates!](/_images/image (1245).png>)
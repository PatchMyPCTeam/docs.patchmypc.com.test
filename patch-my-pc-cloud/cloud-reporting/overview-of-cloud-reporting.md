# Overview of Cloud Reporting

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

The _Reporting_ feature of Patch My PC (PMPC) Cloud allows you to see a wealth of information about your organization that you can use to monitor, maintain, and enhance your environment.

The <strong>Reporting</strong> node consists of the following sub-nodes, each of which contains the most common datasets organizations typically want to report on:

* <strong>Dashboard -</strong> Contains a summary of all of the information from the other tabs.
* <strong>Software Updates -</strong> Contains a summary of the most common software update-related information.
* <strong>Hardware -</strong> Contains a summary of the most common hardware-related information.
* <strong>Intune  -</strong> Contains a summary of the most common information from your Intune tenant.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The sub-nodes you see are determined by the license your PMPC Cloud company is running:</p>
<p>* <strong>Enterprise Plus -</strong> You will only see the <strong>Intune</strong> sub-node.</p>
<p>* <strong>Enterprise Premium –</strong> You will see all sub-nodes.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>The data in the <strong>Intune</strong> sub-node is populated using Microsoft Graph calls to your Intune tenant.</p>
<p>For data to appear and update in the other Reporting sub-nodes, you need to install our client on any devices you wish to collect data from. See [Patch My PC Client](../cloud-administration/manage-client-deployment.md) for more information.</p>
</blockquote>

See [Working with Cloud Reporting](working-with-cloud-reporting.md) for more details on working with the data presented by the Reporting feature.
# Role Scope Tags (optional)

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Using the <strong>Role Scope Tags</strong> tool is optional.</p>
</blockquote>

The <strong>Role Scope Tags</strong> tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to leverage Intune Role Scope Tags (Scope Tags) in your deployments to help control which Intune admins can manage a specific deployment.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Before you can use a Scope Tag in a PMPC Cloud deployment, it must have already been created in the Intune admin center. Follow the <a href="https://learn.microsoft.com/en-us/mem/intune/fundamentals/scope-tags#to-create-a-scope-tag">To create a scope tag</a> process of <a href="https://learn.microsoft.com/en-us/mem/intune/fundamentals/scope-tags">Use role-based access control (RBAC) and scope tags for distributed IT</a> for more details and information on Scope Tags.</p>
<p>If you manage Intune using PMPC Cloud, you should avoid performing any actions in the Intune admin center that can be performed in PMPC Cloud, as doing so will cause unwanted behavior.</p>
</blockquote>

To add Role Scope tag&#x73;<strong>:</strong>

1. Click the <strong>Role Scope Tags</strong> tool.

![Clicking the &#x22;Role Scope Tags&#x22; tool](/_images/image-(78).png "Clicking the &#x22;Role Scope Tags&#x22; tool")

2. Scroll down to the <strong>Role Scope Tags</strong> section.

![Scrolling down to the “Role Scope Tags” section](/_images/image-(79).png "Scrolling down to the “Role Scope Tags” section")

3. In the <strong>Profile Name</strong> field, either:
   1. Start typing the name of the relevant Scope Tag, then click the checkbox beside it to select it.
   2. Click the dropdown to see a list of existing Scope Tags and click the relevant checkbox(es) to select it.

![Selecting the check boxes beside the relevant Scope Tags](/_images/image-(80).png "Selecting the check boxes beside the relevant Scope Tags")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can click the <strong>X</strong> beside a Scope Tag in the <strong>Profile Name</strong> field to delete it.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [Check Scope Tag Assignments](../../../cloud-reference/intune-reference/check-scope-tag-assignments-in-intune.md) for details on how to check within Intune that the Scope Tags defined in the deployment have been assigned correctly.</p>
</blockquote>

4. If you do not want to configure any of the optional tabs under the <strong>Tools</strong> section, click <strong>Next</strong> to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
   \
   Otherwise, click on the relevant tab under <strong>Tools</strong> to configure the required settings, which are explained in the relevant process.

![Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page](/_images/image-(81).png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page")
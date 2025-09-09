# Categories (Deployments)

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Using the <strong>Categories</strong> tool is optional.</p>
</blockquote>

The <strong>Categories</strong> tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to leverage Intune App Categories (Categories) in your deployments to help users find apps in the Company Portal.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See the <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-add#create-and-edit-categories-for-apps">Create and edit categories for apps</a> section of <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-add">Add apps to Microsoft Intune</a> for more information on App Categories.</p>
</blockquote>

To add a Category to a deployment:

1. Click the <strong>Categories</strong> tool.

![Clicking the “Categories” tool](/_images/image-(72).png "Clicking the “Categories” tool")

2. Scroll down to the <strong>Categories</strong> section.

![Scrolling down to the &#x22;Categories&#x22; section](/_images/image-(73).png "Scrolling down to the &#x22;Categories&#x22; section")

3. Go to Step 6. to add a new category or in the <strong>Add Category</strong> field, either:
   1. Start typing the name of the relevant Category, then click the checkbox beside it to select it.
   2. Click the dropdown to see a list of existing Categories and click the relevant checkbox(es) to select it.

![Selecting the checkbox beside the relevant categories](/_images/image-(74).png "Selecting the checkbox beside the relevant categories")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can click the <strong>X</strong> beside a Category in the <strong>Add Category</strong> field to delete it from the list.</p>
</blockquote>

4. Repeat this process to add any additional categories.
5. Go to to step 8. if you do not want to add a new Category.
6. To add a new Category, type its name in the <strong>Add Category</strong> field.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You can create up to 200 categories per Intune tenant. Each category name must:</p>
<p>* Be unique</p>
<p>* Be less than 255 characters</p>
<p>* Not contain the backslash (<strong>\\</strong>) or quote (<strong>"</strong>) characters</p>
<p>* Not be the name of a script.</p>
</blockquote>

![](/_images/image-(75).png "")

7. Press `ENTER` and the <strong>Success – The category “<</strong>_<strong>category\_name></strong>_<strong>” has been created</strong> notification is shown, confirming the new category has been added to both Intune and this deployment.

![](/_images/image-(76).png "")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [Check App Categories](../../../cloud-reference/intune-reference/check-app-categories-in-intune.md) for details on how to check within Intune that the Categories defined in the deployment have been assigned correctly.</p>
<p>Also:</p>
<p>* If different Categories are configured in the portal and Intune admin center they are combined to be the same.</p>
<p>* If a Category is created in the portal and then removed from the Intune admin center, it will be re-added by the portal.</p>
<p>* Categories are also copied forward to a new version of an app.</p>
</blockquote>

8. If you do not want to configure any of the optional tabs under the <strong>Tools</strong> section, click <strong>Next</strong> to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
   \
   Otherwise, click on the relevant tab under <strong>Tools</strong> to configure the required settings, which are explained in the relevant process.

![Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page](/_images/image-(77).png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page")
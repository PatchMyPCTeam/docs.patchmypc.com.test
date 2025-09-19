# Modify/Recreate Cloud Branding

_Applies to: Patch My PC Cloud_

Once you have created a branding app in Patch My PC (PMPC) Cloud, you can modify it as follows:

1. Navigate to <strong>Settings | Branding</strong>

![Navigating  to TSettings | Branding&#x22;](/_images/image-(2411).png "Navigating  to TSettings | Branding&#x22;")

2. Click the ellipsis (`⋮`) button beside the relevant branding app and select the action you want to perform:
   1. [Edit](modify-recreate-cloud-branding.md#edit-branding)
   2. [Recreate](modify-recreate-cloud-branding.md#recreate-branding)

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [Delete Branding](delete-cloud-branding.md) for details on how to delete a branding app.</p>
<p>You won’t be able to manage a branding app until it has been deployed successfully.</p>
<p>Also, see [Managing Localizations](manage-localizations-in-cloud.md) for details on how to modify the localization used by a branding app.</p>
</blockquote>

### Edit Branding

Editing a branding app allows you to make any changes as though you were [Adding a Branding App](add-cloud-branding.md).

If you want to reset the logo used by a branding app:

1. Click <strong>Edit</strong> on the ellipsis (`⋮`) menu.

![Clicking the ellipsis (⋮) button beside the relevant branding app and selecting the action you want to perform:](/_images/image-(2659).png "Clicking the ellipsis (⋮) button beside the relevant branding app and selecting the action you want to perform:")

2. In the <strong>Company Logo</strong> area, click <strong>Use Default</strong>.

![Clicking &#x22;Use Default&#x22; in the &#x22;Company Logo&#x22; area](/_images/image-(2413).png "Clicking &#x22;Use Default&#x22; in the &#x22;Company Logo&#x22; area")

The <strong>Branding</strong> page resets just the logo to the default for this branding app.

![Branding logo reset](/_images/image-(2414).png "Branding logo reset")

3. Make any other required changes.
4. Click <strong>Save</strong> to save your changes to Intune, which will deploy the modified version to all of the resources this branding app is assigned to.

![Clicking &#x22;Save&#x22; to save your changes](/_images/image-(2415).png "Clicking &#x22;Save&#x22; to save your changes")

The <strong>Success - Branding updated</strong> notification is shown.

![&#x22;Success - Branding updated&#x22; notification](/_images/image-(2680).png "&#x22;Success - Branding updated&#x22; notification")

Once your branding app has been updated with the default PMPC logo, the <strong>Status</strong> and <strong>Last Update</strong> fields will be updated to show when this branding app was last updated.

![&#x22;Status&#x22; and &#x22;Last Update&#x22; fields updated to show when this branding app was last updated](/_images/image-(2681).png "&#x22;Status&#x22; and &#x22;Last Update&#x22; fields updated to show when this branding app was last updated")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you look in the <strong>Events</strong> section, you see a message stating the branding app was updated.</p>
</blockquote>

5. The branding app will be automatically updated on all of the assigned resources. There is no need for you to [Recreate Branding](modify-recreate-cloud-branding.md#recreate-branding) as in previous versions..

### Recreate Branding

The <strong>Recreate</strong> function allows you to delete and recreate a branding app in Intune if you detect an issue with it.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You can only recreate branding apps that have either been deployed successfully or have failed.</p>
</blockquote>

To recreate branding:

1. Click <strong>Recreate</strong> on the ellipsis (`⋮`) menu.

![Clicking &#x22;Recreate&#x22; on the ellipsis (⋮) menu](/_images/image-(2682).png "Clicking &#x22;Recreate&#x22; on the ellipsis (⋮) menu")

2. On the <strong>Are you sure you want to recreate <</strong>_<strong>branding\_app\_name</strong>_<strong>></strong> dialog box click <strong>Yes</strong>.

![Clicking &#x22;Yes&#x22;](/_images/image-(2503).png "Clicking &#x22;Yes&#x22;")

The <strong>Success - Recreating the branding <</strong>_<strong>branding\_app\_name</strong>_<strong>></strong> notification is shown.

![](/_images/image-(2683).png "")

Once the branding app has been recreated, the <strong>Status</strong> and <strong>Last update</strong> fields update to show when this branding app was last modified.

![&#x22;Status&#x22; and &#x22;Last update&#x22; fields updated to show when this branding app was last modified](/_images/image-(2684).png "&#x22;Status&#x22; and &#x22;Last update&#x22; fields updated to show when this branding app was last modified")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you look in the <strong>Events</strong> node, you see a message stating the branding app was recreated</p>
</blockquote>
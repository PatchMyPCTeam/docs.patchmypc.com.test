# Modify/Recreate Cloud Branding

_Applies to: Patch My PC Cloud_

Once you have created a branding app in Patch My PC (PMPC) Cloud, you can modify it as follows:

1. Navigate to **Settings | Branding**

![Navigating  to TSettings | Branding&#x22;](/_images/image-(2411).png "Navigating  to TSettings | Branding&#x22;")

2. Click the ellipsis (`⋮`) button beside the relevant branding app and select the action you want to perform:
   1. [Edit](modify-recreate-cloud-branding.md#edit-branding)
   2. [Recreate](modify-recreate-cloud-branding.md#recreate-branding)

{% hint style="info" %}
**Note**

See [Delete Branding](delete-cloud-branding.md) for details on how to delete a branding app.

You won’t be able to manage a branding app until it has been deployed successfully.

Also, see [Managing Localizations](manage-localizations-in-cloud.md) for details on how to modify the localization used by a branding app.
{% endhint %}

### Edit Branding

Editing a branding app allows you to make any changes as though you were [Adding a Branding App](add-cloud-branding.md).

If you want to reset the logo used by a branding app:

1. Click **Edit** on the ellipsis (`⋮`) menu.

![Clicking the ellipsis (⋮) button beside the relevant branding app and selecting the action you want to perform:](/_images/image-(2659).png "Clicking the ellipsis (⋮) button beside the relevant branding app and selecting the action you want to perform:") button beside the relevant branding app and selecting the action you want to perform:")

2. In the **Company Logo** area, click **Use Default**.

![Clicking &#x22;Use Default&#x22; in the &#x22;Company Logo&#x22; area](/_images/image-(2413).png "Clicking &#x22;Use Default&#x22; in the &#x22;Company Logo&#x22; area")

The **Branding** page resets just the logo to the default for this branding app.

![Branding logo reset](/_images/image-(2414).png "Branding logo reset")

3. Make any other required changes.
4. Click **Save** to save your changes to Intune, which will deploy the modified version to all of the resources this branding app is assigned to.

![Clicking &#x22;Save&#x22; to save your changes](/_images/image-(2415).png "Clicking &#x22;Save&#x22; to save your changes")

The **Success - Branding updated** notification is shown.

![&#x22;Success - Branding updated&#x22; notification](/_images/image-(2680).png "&#x22;Success - Branding updated&#x22; notification")

Once your branding app has been updated with the default PMPC logo, the **Status** and **Last Update** fields will be updated to show when this branding app was last updated.

![&#x22;Status&#x22; and &#x22;Last Update&#x22; fields updated to show when this branding app was last updated](/_images/image-(2681).png "&#x22;Status&#x22; and &#x22;Last Update&#x22; fields updated to show when this branding app was last updated")

{% hint style="success" %}
**Tip**

If you look in the **Events** section, you see a message stating the branding app was updated.
{% endhint %}

5. The branding app will be automatically updated on all of the assigned resources. There is no need for you to [Recreate Branding](modify-recreate-cloud-branding.md#recreate-branding) as in previous versions..

### Recreate Branding

The **Recreate** function allows you to delete and recreate a branding app in Intune if you detect an issue with it.

{% hint style="danger" %}
**Important**

You can only recreate branding apps that have either been deployed successfully or have failed.
{% endhint %}

To recreate branding:

1. Click **Recreate** on the ellipsis (`⋮`) menu.

![Clicking &#x22;Recreate&#x22; on the ellipsis (⋮) menu](/_images/image-(2682).png "Clicking &#x22;Recreate&#x22; on the ellipsis (⋮) menu") menu")

2. On the **Are you sure you want to recreate <**_**branding\_app\_name**_**>** dialog box click **Yes**.

![Clicking &#x22;Yes&#x22;](/_images/image-(2503).png "Clicking &#x22;Yes&#x22;")

The **Success - Recreating the branding <**_**branding\_app\_name**_**>** notification is shown.

![](/_images/image-(2683).png "")

Once the branding app has been recreated, the **Status** and **Last update** fields update to show when this branding app was last modified.

![&#x22;Status&#x22; and &#x22;Last update&#x22; fields updated to show when this branding app was last modified](/_images/image-(2684).png "&#x22;Status&#x22; and &#x22;Last update&#x22; fields updated to show when this branding app was last modified")

{% hint style="success" %}
**Tip**

If you look in the **Events** node, you see a message stating the branding app was recreated
{% endhint %}

# Edit an MSP App Set

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

This documentation is under construction. Once it is finalized, this banner will be removed.
{% endhint %}

To edit an MSP App Set:

{% hint style="info" %}
**Note**

You can only edit App Sets that have been created successfully. You will be unable to edit it if it is in any other state (e.g. **Failed**, **In Progress**, **Deleting**, etc.).
{% endhint %}

1.  Navigate to **App Sets**\


    <figure><img src="../../../_images/gitbook/image%20%28111%29.png" alt="Navigating to “App Sets”" width="563"><figcaption></figcaption></figure>
2.  Click the ellipsis (**⋮**) beside the App Set you want to edit and select **Edit**\


    <figure><img src="../../../_images/gitbook/image%20%28112%29.png" alt="Clicking the ellipsis beside the App Set you want to edit" width="563"><figcaption></figcaption></figure>
3. Make any required changes such as:
   1. Editing the name of the App Set
   2. Editing or deleting apps and assignments
   3. Adding new apps and assignments (including adding additional companies to deploy this App Set to).
   4. Modifying the update rings (enabling, disabling, adding rings, removing rings, changing delays for rings, etc.).
4. Once you have finished making your changes, click **Deploy**

{% hint style="info" %}
**Note**

Adding either a new customer or a new app to an App Set triggers a new deployment of the relevant apps to the relevant customers. During this time, the App Set and any relevant deployments will have a **Status** of **In Progress**.

Also, deleting a company from an App Set removes all of the deployments for the apps within that App Set from the relevant company.
{% endhint %}

<figure><img src="../../../_images/gitbook/image%20%28113%29.png" alt="Clicking “Deploy”" width="563"><figcaption></figcaption></figure>

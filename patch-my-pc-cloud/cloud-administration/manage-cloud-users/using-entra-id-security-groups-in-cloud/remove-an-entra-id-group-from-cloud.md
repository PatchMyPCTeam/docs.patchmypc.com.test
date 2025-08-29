# Remove an Entra ID Group from Cloud

_Applies to: Patch My PC Cloud_

{% hint style="warning" %}
**Important**

When you remove an Entra ID Security Group, you are only removing that group’s access to your Patch My PC (PMPC) Cloud Company. You are not deleting the group from Entra ID.
{% endhint %}

To remove an Entra ID Security Group from PMPC Cloud:

1.  In the PMPC Cloud portal, navigate to **Settings | Users**.\


    <figure><img src="../../../../_images/gitbook/image%20%282234%29.png" alt="Navigating to “Settings | Users”"><figcaption></figcaption></figure>


2.  Click the **Entra ID Groups** tab.\


    <figure><img src="../../../../_images/gitbook/image%20%282235%29.png" alt="Clicking the “Entra ID Groups” tab"><figcaption></figcaption></figure>


3. Click the trashcan beside the relevant Entra ID Security Group you want to remove.

{% hint style="warning" %}
**Important**

You need to have at least one user or Entra ID Security Group assigned the **Full Admin with Access Management** user role at all times. You will be unable to delete an Entra ID Security Group assigned this role unless you have either one other user or Entra ID Security Group assigned this role.
{% endhint %}

<figure><img src="../../../../_images/gitbook/image%20%282236%29.png" alt="Clicking the trashcan beside the relevant Entra group you want to delete"><figcaption></figcaption></figure>

4. On the **Are you sure you want to delete <**_**group\_name**_**>** dialog box, click **Yes** to confirm the removal.

<figure><img src="../../../../_images/gitbook/image%20%282237%29.png" alt="Clicking “Yes” to confirm the deletion on the “Are you sure you want to delete <group_name>” dialog box" width="451"><figcaption></figcaption></figure>

\
The portal auto-refreshes to show the group has been removed and the **Success – Group deleted** notification is shown.

<figure><img src="../../../../_images/gitbook/image%20%282238%29.png" alt="Portal auto-refreshing to show the group has been removed and the “Success – Group deleted” notification is shown"><figcaption></figcaption></figure>

When you remove an Entra ID Security Group, the **Group Role Removed** event is written to the **Events** node.

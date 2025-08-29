# Add an Entra ID Group to Cloud

_Applies to: Patch My PC Cloud_

To add an Entra ID Security Group to Patch My PC (PMPC) Cloud:

1. Create the relevant group in Entra ID and add the relevant users.

{% hint style="info" %}
**Note**

We recommend you create an Entra ID group for each [PMPC Cloud User Role](../cloud-user-roles-reference.md) you plan to use.
{% endhint %}

2.  In the PMPC Cloud portal, navigate to **Settings | Users**.\


    <figure><img src="../../../../_images/gitbook/image (2239).png" alt="Navigating to “Settings | Users”"><figcaption></figcaption></figure>


3.  Click **Add Group**.\


    <figure><img src="../../../../_images/gitbook/image (2240).png" alt="Clicking “Add Group”"><figcaption></figcaption></figure>


4.  On the **Available Groups** screen, click the checkbox beside the relevant Entra ID Security Group you want to add, then select the PMPC Cloud role you want to assign to this group from the **Role** dropdown.\


    <figure><img src="../../../../_images/gitbook/image (2241).png" alt="Selecting the relevant Entra ID group to add and which role it will be assigned in PMPC Cloud"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

If you assign an Entra ID Security Group the **Full Admin with Access Management** role, all of this group’s members will receive notifications such as access requests, new version notifications for Binary Free apps (if configured), claim ownership notifications, etc.
{% endhint %}

The selected Entra ID Security Group and role you’ve assigned it in your portal is shown.

<figure><img src="../../../../_images/gitbook/image (2242).png" alt="Selected Entra ID Security Group and role you’ve assigned it in your portal is shown" width="563"><figcaption></figcaption></figure>

5. Repeat Step 4 to add any additional groups/roles.

{% hint style="warning" %}
**Important**

In the current release, you can add up to ten Entra ID Security Groups.
{% endhint %}

6.  Click **Add Group**.\


    <figure><img src="../../../../_images/gitbook/image (2243).png" alt="Clicking “Add Group”"><figcaption></figcaption></figure>

    \
    The portal auto-refreshes, showing the selected groups have been added and the **Success – Group created** notification is shown.\


    <figure><img src="../../../../_images/gitbook/image (2244).png" alt="Portal auto-refreshes, showing the selected groups have been added and the “Success – Group created” notification is shown"><figcaption></figcaption></figure>

When you add an Entra ID Security Group, the **Group role with id <**_**entra\_id\_security\_group\_id**_**> was created with role <**_**user\_role**_**>** event is written to the **Events** node.

{% hint style="info" %}
**Note**

If a user is a member of one or more Entra ID Security Groups assigned different roles, their effective role will be a combination of all the roles assigned to any Entra ID Groups they are a member of.

Likewise, if a user has been added directly to the portal using the [Add a User](../add-a-cloud-user.md) process and they are also a member of one or more Entra ID Security Groups assigned different roles, the same applies, i.e., their effective role will be a combination of all of the roles assigned to them directly in the portal and to any Entra ID Groups they are a member of.
{% endhint %}

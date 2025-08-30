# Add an Entra ID Group to Cloud

_Applies to: Patch My PC Cloud_

To add an Entra ID Security Group to Patch My PC (PMPC) Cloud:

1. Create the relevant group in Entra ID and add the relevant users.

{% hint style="info" %}
**Note**

We recommend you create an Entra ID group for each [PMPC Cloud User Role](../cloud-user-roles-reference.md) you plan to use.
{% endhint %}

2.  In the PMPC Cloud portal, navigate to **Settings | Users**.\


    ![Navigating to “Settings | Users”](../../../../_images/image%20%282239%29.png%20"Navigating%20to%20\"Settings%20|%20Users\"")


3.  Click **Add Group**.\


    ![Clicking “Add Group”](../../../../_images/image%20%282240%29.png%20"Clicking%20\"Add%20Group\"")


4.  On the **Available Groups** screen, click the checkbox beside the relevant Entra ID Security Group you want to add, then select the PMPC Cloud role you want to assign to this group from the **Role** dropdown.\


    ![Selecting the relevant Entra ID group to add and which role it will be assigned in PMPC Cloud](../../../../_images/image%20%282241%29.png%20"Selecting%20the%20relevant%20Entra%20ID%20group%20to%20add%20and%20which%20role%20it%20will%20be%20assigned%20in%20PMPC%20Cloud")

{% hint style="info" %}
**Note**

If you assign an Entra ID Security Group the **Full Admin with Access Management** role, all of this group’s members will receive notifications such as access requests, new version notifications for Binary Free apps (if configured), claim ownership notifications, etc.
{% endhint %}

The selected Entra ID Security Group and role you’ve assigned it in your portal is shown.

![Selected Entra ID Security Group and role you’ve assigned it in your portal is shown](../../../../_images/image%20%282242%29.png%20"Selected%20Entra%20ID%20Security%20Group%20and%20role%20you’ve%20assigned%20it%20in%20your%20portal%20is%20shown")

5. Repeat Step 4 to add any additional groups/roles.

{% hint style="warning" %}
**Important**

In the current release, you can add up to ten Entra ID Security Groups.
{% endhint %}

6.  Click **Add Group**.\


    ![Clicking “Add Group”](../../../../_images/image%20%282243%29.png%20"Clicking%20\"Add%20Group\"")

    \
    The portal auto-refreshes, showing the selected groups have been added and the **Success – Group created** notification is shown.\


    ![Portal auto-refreshes, showing the selected groups have been added and the “Success – Group created” notification is shown](../../../../_images/image%20%282244%29.png%20"Portal%20auto-refreshes,%20showing%20the%20selected%20groups%20have%20been%20added%20and%20the%20\"Success%20–%20Group%20created\"%20notification%20is%20shown")

When you add an Entra ID Security Group, the **Group role with id <**_**entra\_id\_security\_group\_id**_**> was created with role <**_**user\_role**_**>** event is written to the **Events** node.

{% hint style="info" %}
**Note**

If a user is a member of one or more Entra ID Security Groups assigned different roles, their effective role will be a combination of all the roles assigned to any Entra ID Groups they are a member of.

Likewise, if a user has been added directly to the portal using the [Add a User](../add-a-cloud-user.md) process and they are also a member of one or more Entra ID Security Groups assigned different roles, the same applies, i.e., their effective role will be a combination of all of the roles assigned to them directly in the portal and to any Entra ID Groups they are a member of.
{% endhint %}

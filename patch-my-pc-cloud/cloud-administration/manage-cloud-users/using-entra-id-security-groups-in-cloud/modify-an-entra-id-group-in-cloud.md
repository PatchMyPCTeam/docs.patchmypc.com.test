# Modify an Entra ID Group in Cloud

_Applies to: Patch My PC Cloud_

Once an Entra ID Security Group has been added to Patch My PC (PMPC) Cloud, you can change the role assigned to that group.

{% hint style="info" %}
**Note**

You cannot change the membership of an Entra ID Security Group from within the PMPC Cloud portal.
{% endhint %}

To change the role assigned to an Entra ID Security Group:

1.  In the PMPC Cloud portal, navigate to **Settings | Users**.\


    ![Navigating to “Settings | Users”](../../../../_images/image%20%282245%29.png%20"Navigating%20to%20\"Settings%20|%20Users\"")


2.  Click **Entra ID Groups**.\


    ![Clicking “Entra ID Groups”](../../../../_images/image%20%282246%29.png%20"Clicking%20\"Entra%20ID%20Groups\"")


3. Click the dropdown arrow in the **Group Role** column beside the group whose role you want to modify and select the new role.

{% hint style="warning" %}
**Important**

You will be unable to change the group’s role from **Full Admin with Access Management** to another role if this is the only group assigned that role and no users under the **Active Users** tab have been assigned the **Full Admin with Access Management** role.
{% endhint %}

![Clicking the dropdown arrow in the “Group Role” column beside the group whose role you want to modify and selecting the new role](../../../../_images/image%20%282247%29.png%20"Clicking%20the%20dropdown%20arrow%20in%20the%20\"Group%20Role\"%20column%20beside%20the%20group%20whose%20role%20you%20want%20to%20modify%20and%20selecting%20the%20new%20role")

The portal auto-refreshes to show the new role assigned to the group and the **Success – Role changed** notification is shown.

![Portal auto-refreshing to show the new role assigned to the group and the “Success – Role changed” notification is shown](../../../../_images/image%20%282248%29.png%20"Portal%20auto-refreshing%20to%20show%20the%20new%20role%20assigned%20to%20the%20group%20and%20the%20\"Success%20–%20Role%20changed\"%20notification%20is%20shown")

When you change the role of an Entra ID Security Group, the **Group role with name <**_**group\_name**_**> and id <**_**entra\_id\_security\_group\_id**_**> was changed to role <**_**new\_user\_role**_**>** event is written to the **Events** node.&#x20;

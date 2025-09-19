# Modify an Entra ID Group in Cloud

_Applies to: Patch My PC Cloud_

Once an Entra ID Security Group has been added to Patch My PC (PMPC) Cloud, you can change the role assigned to that group.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You cannot change the membership of an Entra ID Security Group from within the PMPC Cloud portal.</p>
</blockquote>

To change the role assigned to an Entra ID Security Group:

1.  In the PMPC Cloud portal, navigate to <strong>Settings | Users</strong>.\


    ![Navigating to “Settings | Users”](/_images/image-(2245).png "Navigating to “Settings | Users”")


2.  Click <strong>Entra ID Groups</strong>.\


    ![Clicking “Entra ID Groups”](/_images/image-(2246).png "Clicking “Entra ID Groups”")


3. Click the dropdown arrow in the <strong>Group Role</strong> column beside the group whose role you want to modify and select the new role.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You will be unable to change the group’s role from <strong>Full Admin with Access Management</strong> to another role if this is the only group assigned that role and no users under the <strong>Active Users</strong> tab have been assigned the <strong>Full Admin with Access Management</strong> role.</p>
</blockquote>

![Clicking the dropdown arrow in the “Group Role” column beside the group whose role you want to modify and selecting the new role](/_images/image-(2247).png "Clicking the dropdown arrow in the “Group Role” column beside the group whose role you want to modify and selecting the new role")

The portal auto-refreshes to show the new role assigned to the group and the <strong>Success – Role changed</strong> notification is shown.

![Portal auto-refreshing to show the new role assigned to the group and the “Success – Role changed” notification is shown](/_images/image-(2248).png "Portal auto-refreshing to show the new role assigned to the group and the “Success – Role changed” notification is shown")

When you change the role of an Entra ID Security Group, the <strong>Group role with name <</strong>_<strong>group\_name</strong>_<strong>> and id <</strong>_<strong>entra\_id\_security\_group\_id</strong>_<strong>> was changed to role <</strong>_<strong>new\_user\_role</strong>_<strong>></strong> event is written to the <strong>Events</strong> node.&#x20;
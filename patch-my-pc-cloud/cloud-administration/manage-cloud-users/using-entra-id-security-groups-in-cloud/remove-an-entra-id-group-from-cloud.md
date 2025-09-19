# Remove an Entra ID Group from Cloud

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>When you remove an Entra ID Security Group, you are only removing that group’s access to your Patch My PC (PMPC) Cloud Company. You are not deleting the group from Entra ID.</p>
</blockquote>

To remove an Entra ID Security Group from PMPC Cloud:

1.  In the PMPC Cloud portal, navigate to <strong>Settings | Users</strong>.\


    ![Navigating to “Settings | Users”](/_images/image-(2234).png "Navigating to “Settings | Users”")


2.  Click the <strong>Entra ID Groups</strong> tab.\


    ![Clicking the “Entra ID Groups” tab](/_images/image-(2235).png "Clicking the “Entra ID Groups” tab")


3. Click the trashcan beside the relevant Entra ID Security Group you want to remove.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You need to have at least one user or Entra ID Security Group assigned the <strong>Full Admin with Access Management</strong> user role at all times. You will be unable to delete an Entra ID Security Group assigned this role unless you have either one other user or Entra ID Security Group assigned this role.</p>
</blockquote>

![Clicking the trashcan beside the relevant Entra group you want to delete](/_images/image-(2236).png "Clicking the trashcan beside the relevant Entra group you want to delete")

4. On the <strong>Are you sure you want to delete <</strong>_<strong>group\_name</strong>_<strong>></strong> dialog box, click <strong>Yes</strong> to confirm the removal.

![](/_images/image-(2237).png "")

\
The portal auto-refreshes to show the group has been removed and the <strong>Success – Group deleted</strong> notification is shown.

![Portal auto-refreshing to show the group has been removed and the “Success – Group deleted” notification is shown](/_images/image-(2238).png "Portal auto-refreshing to show the group has been removed and the “Success – Group deleted” notification is shown")

When you remove an Entra ID Security Group, the <strong>Group Role Removed</strong> event is written to the <strong>Events</strong> node.
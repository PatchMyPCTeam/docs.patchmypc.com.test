# “Group not found” shown for an Assignment of a successful Cloud deployment

_Applies to: Intune Apps for Cloud_

### SYMPTOMS

I’ve successfully deployed an app using Intune Apps for Cloud (Intune Apps). However, when I look at its properties (by clicking on the deployment, pressing <strong>More Info</strong>, and expanding the <strong>Assignment Type</strong>), why does it show <strong>(Group not found)</strong> beside the assignment?

![&#x22;Group not found&#x22; shown beside the assignment for a successful assignment.](/_images/image-(366).png "&#x22;Group not found&#x22; shown beside the assignment for a successful assignment.")

If I edit the deployment and click <strong>Assignments</strong>, I also see the <strong>Group not found. Please remove the assignment</strong> message.

![&#x22;Group not found. Please remove the assignment&#x22; message](/_images/image-(365).png "&#x22;Group not found. Please remove the assignment&#x22; message")

### CAUSE

This is because someone has deleted the group used for the assignment from Entra.

### RESOLUTION

To resolve this issue:

1. Recreate and reconfigure the relevant group in Entra.
2. Edit the deployment in the portal.
3. Delete the relevant assignment.
4. Re-add the assignment by browsing to the recreated Entra group.
5. Complete the deployment.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Even though the group has been recreated in Entra with the same name, it will have a different Object Id so the original assignment has to be deleted and recreated to pick up the new group with the new Object Id.</p>
<p>See the [Edit a Deployment](../../cloud-deployments/manage-cloud-deployments/edit-a-cloud-deployment.md) process for more details.</p>
</blockquote>
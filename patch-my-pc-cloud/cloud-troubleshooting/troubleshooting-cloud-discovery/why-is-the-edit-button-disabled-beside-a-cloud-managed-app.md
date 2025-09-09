# Why is the “Edit” button disabled beside a Cloud Managed App?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I have signed into the Patch My PC (PMPC) Cloud portal and navigated to the <strong>Discovery</strong> node, followed by the <strong>Managed</strong> tab.

I see the list of my managed apps, but why is the <strong>Edit</strong> button beside my app greyed out?

### CAUSE

This can occur for several reasons, including:

* The <strong>Status</strong> of the app is not showing as <strong>Success</strong> (it is in a <strong>In Progress</strong>, <strong>Failed</strong> or <strong>Retrying</strong> state).
* The signed in user does not have permission to edit deployments.
* Your PMPC Cloud portal license has expired.
* The deployment was made using our on-premises Publisher.

### RESOLUTION

To resolve this issue:

1. Check the <strong>Status</strong> of the relevant deployment. If it is showing as <strong>Failed</strong>, follow the [Troubleshooting an Intune Apps Deployment](../troubleshooting-cloud-deployments/troubleshooting-an-intune-apps-deployment.md) process.
2. Verify the user has not been assigned the <strong>Custom App Admin</strong> user role, as this role cannot edit deployments.
3. Follow the [Managing your License](../../cloud-administration/manage-your-environments-in-cloud/manage-your-cloud-license.md) process to verify your license is still valid.
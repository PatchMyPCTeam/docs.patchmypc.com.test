# "Error - Claim Ownership Failed" when trying to recover a Cloud Company

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I can no longer access my Patch My PC (PMPC) Cloud Company as the only admin has left and no other users have been created with the <strong>Full Admin with Access Management</strong> role.

I have tried running through the [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) process, but after entering the requested information, I see the following:

<strong>Error</strong>

<strong>Claim Ownership Failed</strong>

![“Error - Claim Ownership Failed”](/_images/image-(1959).png "“Error - Claim Ownership Failed”")

### CAUSE

This error can occur for several reasons, such as:

1. You have entered invalid data to attempt the recovery.
2. You are trying to recover a PMPC Company from the wrong Entra ID tenant.

### RESOLUTION

To resolve this issue:

1. Verify you are entering the right values in the correct fields of the <strong>Claim Ownership</strong> wizard.
2. Verify that the last five characters shown for the company you are trying to recover match the last five characters of the Entra ID tenant (the <strong>Directory (tenant) ID</strong>).

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You only have three attempts to complete the <strong>Claim Ownership</strong> wizard. After the third failed attempt, you will see the following error:</p>
<p><strong>You've reached the maximum number of claim ownership attempts. Please try again later.</strong></p>
<p>You will be locked out and prevented from attempting the recovery for 12 hours.</p>
</blockquote>
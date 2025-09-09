---
description: >-
  Next, we want to verify that the third-party updates appear in the WSUS
  Console.
---

# Verify Third-Party Updates Appear in WSUS Console

_Applies to: On-premises Publisher_

Any updates published after the WSUS Standalone option was enabled should appear directly in the WSUS console.

![](/_images/image-(1133).png>)

<blockquote class="wp-block-quote">
<p><strong>Note:</strong> If updates were published <strong>before this setting was enabled</strong>, they would <strong>not appear in the WSUS console automatically</strong>.</p>
<p>For updates published before WSUS Standalone mode was enabled, use the <a href="https://patchmypc.com/modify-published-third-party-updates-wizard"><strong>Modify Published Updates Wizard</strong></a> to make those updates appear in the WSUS console.</p>
</blockquote>

### Adding an Update View for Patch My PC Updates

We can also create a new <strong>Update View</strong> for Patch My PC updates. This will help with finding and managing updates from Patch My PC within WSUS.&#x20;

We'll walk through that process in the steps below:

* In WSUS right-click <strong>Updates</strong> and select <strong>New Update View...</strong>
* Under Step 1, select <strong>Updates are for a specific product</strong>
* Under Step 2, select <strong>any product</strong>
* In the <strong>Choose Products</strong> window, check the <strong>All Products</strong> box at the top to disable all products. Scroll down to the bottom of the list, enable the boxes for <strong>Patch My PC</strong> and <strong>SCUP Updates,</strong> and select <strong>OK</strong>
* For Step 3, specify a name, for example: <strong>Patch My PC Updates,</strong> and select <strong>OK</strong>
* Select <strong>Patch My PC Updates</strong>
* If needed, change <strong>Approval</strong> to <strong>Any Except Declined</strong> and <strong>Status</strong> to <strong>Any</strong>
* Hit <strong>Refresh</strong> and now you will see all of the Patch My PC Updates in that list&#x20;

You can now deploy the third-party updates just like a Microsoft update <strong>directly from the WSUS console</strong>.
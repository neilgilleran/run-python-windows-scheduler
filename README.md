# run-python-windows-scheduler

How to run a python script from windows scheduler

1. Create python script
1. Create batch file
1. Configure Task Scheduler


## Configure Windows Task Scheduler

1. From the Start menu, select Administrative Tools > Task Scheduler.
1. Under Task Scheduler (Local), select Task Scheduler Library and choose New Folder from the Actions panel.
1. Enter "My scedules" and click OK.
1. The new folder is created for your scheduled tasks.
1. Expand Task Scheduler Library and select your folder.
1. In the Actions panel, click Create Basic Task.
1. In the Create a Basic Task dialog, enter a name for the task and click Next.
1. In the Task Trigger dialog, select Daily and click Next.
1. In the Daily dialog, enter the Start date and time, and click Next.
1. In the Action dialog, select Start a program and click Next.
1. In the Program/script field, browse and select the batch file then click Open.
1. For example, enter C:\Users\neil\git\run-python-windows-scheduler\text-batch.bat
1. Click Next.
1. In the Summary dialog, select Open the Properties dialog for this task when I click Finish and then click Finish. The Maintenance Manager Properties dialog opens.
1. If the Properties window for the Maintenance Manager task is not already open, double-click the task name in the Task Scheduler Library.
1. The Properties window opens with the General tab displayed.
1. Select Run whether user is logged on or not.
1. Select Run with highest privileges option.
1. Click OK.
1. Ensure that the Maintenance Manager domain/Windows account is correct, enter the password, then click OK.
1. Click OK to close the Properties window.
1. Close the Task Scheduler.

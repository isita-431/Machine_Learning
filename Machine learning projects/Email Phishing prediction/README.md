The main objective of this project is to check whether the mails content Phishing content or not.
1. First i extracted features such as :
   * whether the mail is a HTML Email or not.
   * how many IP-based URLs the mail contains.
   * if there's presence of javascript in the mail.
   * Presence of Form Tag in the mail.
   * number of domains of the mail.
   * Number of Sub-domains of the mail.
   * if the mail has URL Based Image Source.
   * if the domain is more or less than 30 days.
2. after extracting all the features kmeans clustering is performed to check the different groups these mail belongs to and to check 
   how many mails go into the category of "Phishing content present".

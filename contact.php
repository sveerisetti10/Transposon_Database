<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["Name"];
  $email = $_POST["Email"];
  $subject = $_POST["Subject"];
  $comment = $_POST["Comment"];
  $to = "sv@bu.edu";
  $subject = "New message from " . $name . " (" . $email . ")";
  $message = "Subject: " . $subject . "\n\n" . "Message: " . $comment;
  $headers = "From: " . $email . "\r\n" .
             "Reply-To: " . $email . "\r\n" .
             "X-Mailer: PHP/" . phpversion();
  mail($to, $subject, $message, $headers);
}
?>
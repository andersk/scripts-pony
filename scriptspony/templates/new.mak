<%inherit file="scriptspony.templates.master"/>

<%!
from socket import gethostbyname
%>

<div><a href="${tg.url('/')}">Back to list</a></div>

<form method="post">
  <ul>
    <li>Locker: ${locker}</li>
    <li>Hostname: <input type="text" name="hostname" value="${hostname}" /></li>
    <li>Path: /mit/${locker}/web_scripts/<input type="text" name="path" value="${path}" /></li>
  </ul>
  <input type="submit" value="Request Hostname" />
</form>

<p>
  Notes:
  <ul>
    <li>
      You can request any hostname ending with ".${locker}.scripts.mit.edu"
      freely.
    </li>
    <li>Only some hostnames ending with ".mit.edu" are available, and they
      take a few business days to become active.  You can check whether
      a given mit.edu hostname is available by typing "stella &lt;hostname&gt;"
      from an Athena prompt.</li>
    <li>You can request a non-MIT hostname, but you'll have to
      register the hostname yourself and configure it with a CNAME
      record for scripts-vhosts.mit.edu or an A record for
      scripts-vhosts.mit.edu's IP address,
      ${gethostbyname('scripts-vhosts.mit.edu')}.</li>
  </ul>
</p>

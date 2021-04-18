# Frequently Asked Questions
If you have a question and you can't find it here, please ask it in an issue.

#### Question: I'm getting a `401 Unauthorized` error. What's wrong?
Check whether you have set your token correctly and that it has permission in
[Ocean](ocean.sotoon.ir). If it's all good, it's probably because you're using
a service or a version of it that you haven't ordered yet or you've ran out of
credit. Check [Ocean](ocean.sotoon.ir) for these, too.  
Also, another pitfall is that the `token` you receive from [Ocean](ocean.sotoon.ir)
starts with `service-user:` string. You <b>must not</b> remove this from token value!


#### Question: Is it bad to create a channel every time I want to send a request?
Yes. Creating a channel means opening a socket and connecting to the server. If
you create a separate channel for every single request, you'll exhaust your
ports and most likely hit the open-file-count limit that's set by your OS. We
suggest you create a single channel and use it for all your requests. But check
the gRPC documentation for your desired language for the thread-safety concerns
of channels.
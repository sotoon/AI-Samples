# Introduction

This is `AI Samples` repository, where you'll learn how to use Sotoon's AI services!

We assume you have downloaded a `.proto` file from
[Ocean](https://ocean.sotoon.ir) and want to use it in your project, but you
don't have enough experience with gRPC and protobuf. Here, we explain how you
can use the `.proto` file in your project. Follow the instructions for your
desired language:
* [Python](./python/)

# AI Services Terminology
We use these terms in the instructions, so please read them before using this
project.

## gRPC
[gRPC](https://grpc.io/docs/) is an open source remote procedure call (RPC)
protocol, that uses HTTP/2 for transport,
[Protocol Buffers](https://developers.google.com/protocol-buffers) as the
interface description language, and provides features such as authentication,
bidirectional streaming and flow control, blocking or non-blocking bindings,
cancellation and timeouts, and a much faster communication compared to REST and
JsonRPC. It generates cross-platform client and server bindings for many
languages. Most common usage scenarios include connecting services in
microservices style architecture and connect mobile devices, browser clients
to backend services.

## Protocol Buffers
Protocol Buffers, A.K.A
[Protobuf](https://developers.google.com/protocol-buffers/docs/overview), is a
protocol for client and server to communicate with each other. You can define
your message types in a `.proto` file and then you use the `protoc` compiler to
compile this file into classes/structs/etc. in your desired language and then
use them in your code.

For example, this proto message:
```protobuf
message SearchRequest {
  string query = 1;
  int32 page_number = 2;
}
```
will be translated to a Python class named `SearchRequest` with `query` and
`page_number` fields.

## Service Header
In order to send requests to different versions of a service, you need to set
the `service` header in your requests. Some services, don't need this because
there's only one version of them, so this is an optional header.

By checking a service's section in [Ocean](https://ocean.sotoon.ir), you can
find out whether it's optional and the possible values.

## Token Header
This header is used for authentication and authorization. Check out
[Ocean](https://ocean.sotoon.ir) to find out how to generate a token and how to
grant your desired permissions to a token.

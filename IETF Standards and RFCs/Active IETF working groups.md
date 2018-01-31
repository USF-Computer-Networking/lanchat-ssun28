# Active IETF working groups

Working Groups (WGs) are the primary mechanism for development of IETF specifications and guidelines, many of which are intended to be standards or recommendations.

Working Groups are typically created with a charter that describes the specific problem or deliverables (a guideline, standards specification, etc.) it has been formed to address. WG charters state the scope of work for group, and lay out goals and milestones that show how this work will be completed.

**Material can be found at [https://www.ietf.org/how/wgs/](https://www.ietf.org/how/wgs/) .**

## DNS Over HTTPS (doh)

**Area** Applications and Real-Time Area (art)

**State**	Active

**Dependencies** [Document dependency graph](https://datatracker.ietf.org/wg/doh/deps/svg/) (SVG)

This working group will standardize encodings for DNS queries and responses
that are suitable for use in HTTPS. This will enable the domain name system to
function over certain paths where existing DNS methods (UDP, TLS [RFC 7857],
and DTLS [RFC 8094]) experience problems.

The working group will re-use HTTPS methods, error codes, and other semantics
to the greatest extent possible. The use of HTTPS and its existing PKI
provides integrity and confidentiality, and it also allows interoperation
with common HTTPS infrastructure and policy.

The primary focus of this working group is to develop a mechanism that
provides confidentiality and connectivity between DNS clients (e.g., operating
system stub resolvers) and recursive resolvers. While access to
DNS-over-HTTPS servers from JavaScript running in a typical web browser is not
the primary use case for this work, precluding the ability to do so would
require additional preventative design. The working group will not engage in
such preventative design.

The working group will analyze the security and privacy issues that
could arise from accessing DNS over HTTPS. In particular, the working
group will consider the interaction of DNS and HTTP caching.

The working group will coordinate with the DNSOP and INTAREA working groups
for input on DNS-over-HTTPS's impact on DNS operations and DNS semantics,
respectvely. In particular, DNSOP will be consulted for guidance on the
operational impacts that result from traditional host behaviors (i.e.,
stub-resolver to recursive-resolver interaction) being replaced with the
specified mechanism.

## IPv6 over Networks of Resource-constrained Nodes (6lo)

**Area** Internet Area (int)

**State**	Active

**Dependencies** [Document dependency graph (SVG)](https://datatracker.ietf.org/wg/6lo/deps/svg/)

6lo focuses on the work that facilitates IPv6 connectivity over constrained node networks with the characteristics of:
* limited power, memory and processing resources
* hard upper bounds on state, code space and processing cycles
* optimization of energy and network bandwidth usage
* lack of some layer 2 services like complete device connectivity and
broadcast/multicast

Specifically, 6lo will work on:


    1. IPv6-over-foo adaptation layer specifications using 6LoWPAN
    technologies (RFC4944, RFC6282, RFC6775) for link layer technologies of
    interest in constrained node networks

    2. Information and data models (e.g., MIB modules) for these
    adaptation layers for basic monitoring and troubleshooting.

    3. Specifications, such as low-complexity header compression, that are
    applicable to more than one adaptation layer specification

    4. Maintenance and informational documents required for the existing
    IETF specifications in this space.

Only specifications targeting constrained node networks are in scope.
6lo will work closely with the 6man working group, which will continue
to work on IP-over-foo documents outside the constrained node network
space and will continue to be the focal point for IPv6 maintenance. For
adaptation layer specifications that do not have implications on IPv6
architecture, 6man will be notified about 6lo's working group last call.
Specifications that might have such an impact (e.g., by using IPv6
addresses in a specific way or by introducing new ND options or by
exposing to IPv6 a link model different from either Ethernet or 6lowpan)
will be closely coordinated with 6man, and/or specific parts will be
fanned out to 6man documents. Beyond 6man, 6lo will also coordinate with
LWIG and INTAREA.

## IP Security Maintenance and Extensions (ipsecme)

**Area** Security Area (sec)

**State**	Active

**Dependencies** [Document dependency graph (SVG)](https://datatracker.ietf.org/wg/ipsecme/deps/svg/)

The IPsec suite of protocols includes IKEv1 (RFC 2409 and associated
RFCs), IKEv2 (RFC 7296), and the IPsec security architecture (RFC
4301). IPsec is widely deployed in VPN gateways, VPN remote access
clients, and as a substrate for host-to-host, host-to-network, and
network-to-network security.

The IPsec Maintenance and Extensions Working Group continues the work
of the earlier IPsec Working Group which was concluded in 2005. Its
purpose is to maintain the IPsec standard and to facilitate discussion
of clarifications, improvements, and extensions to IPsec, mostly to
IKEv2. The working group also serves as a focus point for other IETF
Working Groups who use IPsec in their own protocols.

The current work items include:

IKEv2 contains the cookie mechanism to protect against denial of
service attacks. However this mechanism cannot protect an IKE
end-point (typically, a large gateway) from "distributed denial of
service", a coordinated attack by a large number of "bots". The
working group will analyze the problem and propose a solution, by
offering best practices and potentially by extending the protocol.

IKEv2 utilizes a number of cryptographic algorithms in order to
provide security services. To support interoperability a number of
mandatory-to-implement (MTI) algorithms are defined in RFC4307 for
IKEv2 and in RFC7321 for ESP/AH. There is interest in updating the
MTIs in RFC4307 and RFC7321 based on new algorithms, changes to the
understood security strength of existing algorithms, and the degree of
adoption of previously introduced algorithms. The group will revise
RFC4307 and RFC7321 proposing updates to the MTI algorithms used by
IKEv2 and IPsec to address these changes.

There is interest in supporting Curve25519 and Curve448 for ephemeral
key exchange and EdDSA for authentication in the IKEv2 protocol. The
group will extend the IKEv2 protocol to support key agreement using
these curves and their related functions.

IKEv1 using shared secret authentication was partially resistant to
quantum computers. IKEv2 removed this feature to make the protocol
more usable. The working group will add a mode to IKEv2 or otherwise
modify IKEv2 to have similar quantum resistant properties than IKEv1
had.

### Description of the current working group discussions
##### IP Security Maintenance and Extensions (ipsecme)

    [IPsec] ipsecme - New Meeting Session Request for IETF 101
    IETF Meeting Session Request Tool <session-request@ietf.org> Mon, 29 January 2018 20:48 UTCShow header

    A new meeting session request has just been submitted by Tero Kivinen, a Chair of the ipsecme working group.


    ---------------------------------------------------------
    Working Group Name: IP Security Maintenance and Extensions
    Area Name: Security Area
    Session Requester: Tero Kivinen

    Number of Sessions: 1
    Length of Session(s):  1.5 Hours
    Number of Attendees: 50
    Conflicts to Avoid:
    First Priority: sacm mile tcpinc curdle tls saag cfrg i2nsf
    Second Priority: 6tisch lwig ace
    Third Priority: uta 6lo tcpm netmod


    People who must be present:
    Eric Rescorla
    Tero Kivinen
    David Waltermire

    Resources Requested:

    Special Requests:

    ---------------------------------------------------------

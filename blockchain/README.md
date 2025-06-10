# Blockchain Technology
<p align="center">
<img src="https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" width="700">
</p>

**Blockchain** is a type of **Distributed Ledger Technology (DLT)** that consists of a continuously growing list of records, known as **blocks**, that are securely linked together using **cryptography**. The Blockchain concept was introduced as the foremost foundation of **bitcoin** technology by Sakoshi Nakamoto in 2008. The infamous Nakamoto is an alias for the founder(s) who developed bitcoin, including the bitcoin white paper, as well as the original bitcoin reference implementation. Over time, blockchain technology has developed from a simple cryptocurrency implementation to a foundational technology for secure, transparent, and decentralised system architecture.

Here are the key blockchain terminologies:
- Distributed Ledger Technology (DLT)
- Blocks
- Cryptography

## Distributed Ledger Technology (DLT)
First of all, a **ledger** is a book or collection of accounts that keeps track of account transactions. Usually, ledgers are **centralised**, meaning that they're controlled by a sole influence. These ledgers are physical records maintained by banks, governments, and other establishments to track financial transactions, ownership records, and any other essential information.
However, this approach only serves as a hotbed for inefficiency and over-reliance on a sole entity.

This is where Distributed Ledger Technology comes in. DLT represents a massive shift from centralised data management.

Instead of one single entity managing data, the ledger, which in this case is **digital**, is shared among multiple **nodes**(computers) in a network. Each node is responsible for maintaining an **identical** copy of the main ledger, and all these nodes must consent before any new information is added to the main ledger.

*Key Characteristics of DLT:*
- Decentralisation: No single point of control, management or failure
- Transparency: All network participants can see transactions, although personal details may be encrypted
- Immutability: Once data is recorded and confirmed, it becomes extremely hard to change
- Consensus Mechanisms: Network participants must agree on the credibility of new transactions

*To further conceptualise Distributed Ledger Technology, imagine the scenario below:*
- Four roommates live in an apartment together.
- They all contribute towards groceries, utilities, and rent.
- In the spirit of accountability, they use a **shared Google Sheet** where every expense is tracked.
- Everyone can **see**, **add**, and **validate** expenses, but **no one can delete past expense entries** — they're only allowed to append new rows with reasons for any corrections.

This is exactly how a Distributed Ledger works.

| Google Sheet Feature                              | DLT Concept Equivalent                            |
|---------------------------------------------------|---------------------------------------------------|
| Everyone has access to the same document          | **Distributed ledger** — everyone has a synchronised copy |
| Changes are visible to all in real time           | **Transparency and consensus**                    |
| No one can erase old entries; only new ones can be added with explanations | **Immutability** of records                        |
| Each entry includes a timestamp and who added it  | **Timestamped transactions** and **identity** (like digital signatures) |
| Everyone can verify what’s been entered           | **Decentralised verification**                    |
| Any disputes are resolved by checking the shared record | **Consensus mechanism** (though manual here)   |

## Centralised vs. Distributed Management

**Centralised approach:** Here, an organisation with 4 branches stores all its data in one central database. This database is managed by the Chief Administrator at the headquarters. Each branch needs approval from the Chief Administrator to view and access information. If a bad actor gains access to the central database, they can unduly alter all the data, and if the central database fails, all the branches lose their access to vital data.

**Distributed approach:** In this case, each organisational branch maintains a complete **carbon copy** of the original ledger. For one branch to add information, all branches must reach a consensus. When one branch adds information, it's broadcast to the entire network and systematically synchronised across all other ledgers through a peer-to-peer network after verification.

In summary, a distributed approach offers:
- Fault tolerance: If information is altered in one branch, other branches can detect the change through consensus algorithms
- Security: If one branch is compromised, other branches remain secure and can identify the bad actor
- Availability: No single point of failure — if one computer goes down, the network is still highly functional
- Verification: Any member of the network can independently verify the integrity of the complete transaction history

## Blocks
A **block** is a cluster of transactions grouped together with metadata in a structured manner.
Imagine a block as a page in a digital ledger. This page consists of multiple transaction entries, including important information about when and how that page was created.

*Structure of a Block:*
1. Block Header:
- Previous Block Hash: A unique fingerprint of the previous block, creating the *chain*
- Merkle Root: A cryptographic summary of all transactions in the block
- Timestamp: The time the block was created
- Nonce: A number used in the Proof-of-Work (PoW) mining process
- Difficulty Target: The complexity level required to mine this block

2. Block Body:
- Transaction Data: The actual transaction records (transfers, smart contract executions, etc.)
- Transaction Count: Number of transactions confirmed in the block

## The Chain Formation
Blocks are connected cryptographically using hash functions, in order to create an **immutable** chain:
1. Genesis Block: The first block in the chain, which is hardcoded into the blockchain protocol
2. Subsequent Blocks: Each new block contains the hash function of the preceding block
3. Chain Integrity: If someone tries to modify a previous block, its hash function changes, breaking the chain and notifying the entire network

With cryptographic linking, once a block is added to the chain and verified by the network, modifying any preceding block is computationally impractical. The deeper a block is in the chain (the more blocks built on top of it), the more secure it becomes.

## Cryptography
Cryptography is the practice and study of secure communication strategies that safeguard information from unwanted access. In the context of blockchain, cryptography is the backbone of security, privacy, and trust, in a decentralised network where participants don't know, or even trust each other.

*Key Cryptographic Concepts in Blockchain:*
1. Hash Functions:
- Generate fixed-size output (hash) from variable-size input
- The SHA-256 function is typically used in Bitcoin
- Properties: Deterministic (giving input to a hash function will always produce the same output), avalanche effect, irreversible
- Used for: Block linking, transaction verification, mining puzzles

2. Digital Signatures:
- Prove ownership and authorise transactions without revealing private keys
- Based on public-key cryptography (asymmetric encryption)
- Each user has a pair: private key (secret) and public key (shareable)
- Process: Sign with private key and verify with public key

3. Merkle Trees:
- Binary tree structure that effectively outlines all transactions in a block
- Enables quick verification of transaction inclusion without having to download the entire block
- Provides evidence for altered transaction data

*Cryptographic Security in Practice:*
1. Transaction Security:
When person A wants to send **cryptocurrency** to person B:
- Person A creates a transaction using person B's **public address**
- Person A signs the transaction with their **private key**
- Network nodes verify the signature using person A's **public key**
- Once verified, the transaction is added to a block

2. Block Integrity:
- Each block contains the hash of the previous block
- Any change to a previous block changes its hash
- This breaks the chain and immediately notifies the entire network
- Makes altering historical data unfeasible

3. Privacy vs. Transparency:
- **Transparency** means amounts and addresses are public.
- **Privacy** ensures that real-world identities behind addresses are undisclosed.
- This balance allows for accountability and anonymity in transactions.

> In summary, **Blockchain technology** represents a pioneering shift in how we store, verify, and transfer value in digital systems. It's a distributed, immutable, non-physical ledger that records transactions and tracks assets across a decentralised network, without requiring **trust** in a sole entity.
Blockchain networks can track and trade virtually any **asset** of value, from tangible assets like real estate, commodities, and vehicles, to intangible assets such as cryptocurrencies, intellectual property, digital art (NFTs), and carbon credits.
A blockchain network can track and sell almost anything of value, lowering risk and costs for everyone involved.

This is just a brief introduction to blockchain technology.
To find out more about this technology, check out the links below:
* <https://en.wikipedia.org/wiki/Blockchain> - Comprehensive overview of blockchain technology
* <https://bitcoin.org/bitcoin.pdf> - The original document by Satoshi Nakamoto
* <https://ethereum.org/en/whitepaper/> - Introduction to programmable blockchain
* <https://en.wikipedia.org/wiki/Cryptographic_hash_function> - Understanding the math behind blockchain security
* <https://en.wikipedia.org/wiki/Merkle_tree> - Data structure for efficient verification
* <https://web3js.readthedocs.io/> - JavaScript library for blockchain interaction
* <https://en.wikipedia.org/wiki/Chinese_remainder_theorem>
* <https://en.wikipedia.org/wiki/Diophantine_equation>
* <https://www.geeksforgeeks.org/modular-division/>

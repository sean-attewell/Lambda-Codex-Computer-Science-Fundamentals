# Your computer has something called random access memory (RAM). Sometimes, people say "memory" when referring to RAM.

# There is a distinction between "storage" and "memory". Things like videos and files are stored on a disc, not in RAM. 
# RAM is faster than disc storage, but there isn't as much space available. Disc storage has more space, but it is slower.

# Think of RAM like a set of numbered, sequential mailboxes (memory addresses). 
# Just like a set of mailboxes with numbered addresses, RAM is also sequential and has numbered addresses.

# Now, just like you can put something in a mailbox, you can also put something in RAM. 
# Things that you put in RAM, we can call variables. 

# Each "box"  in RAM has an address.
# Each one of the "boxes" RAM holds 8 bits (1 byte)

# Now, a computer has more than just disc storage and RAM inside of it. There is also a processor. And, in between the processor and the RAM is something called a memory controller. The memory controller can access each box in RAM directly. It is as if the memory controller had tubes connected to each box of the set of mailboxes. Through those tubes, the memory controller can send and receive information directly to each box in RAM.

# Why is the direct connection between the memory controller and each box in RAM meaningful? It's so that the memory controller can jump around to which box it wants to communicate with quickly. Even though the boxes are in sequential order, the memory controller doesn't have to go through the boxes in order. It can access the first one, then jump to one somewhere in the middle, and then access one at the end. Because there is a direct connection, this is done quickly.

# Whenever a processor accesses a box in RAM, it also accesses and stores the boxes near it. Often, if you are accessing one thing in RAM, it's likely that the next thing you need to access is nearby. That's why keeping a copy of nearby items in the cache speeds things up.

# As you can see, the cache helps the processor by saving execution cycles required to go out and read something from RAM.

# The processor, not RAM, has the actual cache. The memory controller keeps track of what goes into and comes out of the cache.

# There is one caveat — it is not as if "everything" goes out to RAM and then gets inserted into the cache. In reality, the cache holds only a handful of memory addresses from RAM.

# https://en.wikipedia.org/wiki/Random-access_memory

# A random-access memory device allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory.

# In contrast, with other direct-access data storage media such as hard disks, CD-RWs, DVD-RWs and the older magnetic tapes and drum memory, the time required to read and write data items varies significantly depending on their physical locations on the recording medium, due to mechanical limitations such as media rotation speeds and arm movement.

# RAM contains multiplexing and demultiplexing circuitry, to connect the data lines to the addressed storage for reading or writing the entry. 
# Usually more than one bit of storage is accessed by the same address, and RAM devices often have multiple data lines and are said to be "8-bit" or "16-bit", etc. devices.

# In today's technology, random-access memory takes the form of integrated circuit (IC) chips with MOS (metal-oxide-semiconductor) memory cells. RAM is normally associated with volatile types of memory (such as dynamic random-access memory (DRAM) modules), where stored information is lost if power is removed, although non-volatile RAM has also been developed.[3] Other types of non-volatile memories exist that allow random access for read operations, but either do not allow write operations or have other kinds of limitations on them. These include most types of ROM and a type of flash memory called NOR-Flash.


# https://en.wikipedia.org/wiki/Memory_controller

# The memory controller is a digital circuit that manages the flow of data going to and from the computer's main memory. A memory controller can be a separate chip or integrated into another chip, such as being placed on the same die or as an integral part of a microprocessor; in the latter case, it is usually called an integrated memory controller (IMC). A memory controller is sometimes also called a memory chip controller (MCC)[1] or a memory controller unit (MCU).[2]

# A common form of memory controller is the memory management unit (MMU) which in many operating systems, such as Unix, implements virtual addressing.


# https://en.wikipedia.org/wiki/CPU_cache

# A CPU cache is a hardware cache used by the central processing unit (CPU) of a computer to reduce the average cost (time or energy) to access data from the main memory.[1] A cache is a smaller, faster memory, located closer to a processor core, which stores copies of the data from frequently used main memory locations. Most CPUs have a hierarchy of multiple cache levels (L1, L2, often L3, and rarely even L4), with separate instruction-specific and data-specific caches at level 1.

# Other types of caches exist (that are not counted towards the "cache size" of the most important caches mentioned above), such as the translation lookaside buffer (TLB) which is part of the memory management unit (MMU) which most CPUs have.

# https://en.wikipedia.org/wiki/Microprocessor

# A microprocessor is a computer processor where the data processing logic and control is included on a single integrated circuit, or a small number of integrated circuits. The microprocessor is a multipurpose, clock-driven, register-based, digital integrated circuit that accepts binary data as input, processes it according to instructions stored in its memory, and provides results (also in binary form) as output. Microprocessors contain both combinational logic and sequential digital logic. Microprocessors operate on numbers and symbols represented in the binary number system.


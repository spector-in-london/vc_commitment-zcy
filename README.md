# Vector Commitments with Incremental Aggregation based on Accumulators

This code is an implementation of some of the constructions in [Vector Commitment Techniques and Applications to Verifiable Decentralized Storage](https://eprint.iacr.org/2020/149) by Campanelli et al..
The accumulator constructions are based on [this paper](https://eprint.iacr.org/2018/1188).



/home/jcq/.cargo/registry/src/mirrors.ustc.edu.cn-61ef6e0cd06fb9b8/backtrace-0.3.56/src/symbolize/gimli.rs:119:        use core::mem::MaybeUninit;
/home/jcq/.cargo/registry/src/mirrors.ustc.edu.cn-61ef6e0cd06fb9b8/ryu-1.0.5/src/buffer/mod.rs:3:use core::mem::MaybeUninit;
/home/jcq/.cargo/registry/src/mirrors.ustc.edu.cn-61ef6e0cd06fb9b8/ryu-1.0.5/src/d2s.rs:30:use core::mem::MaybeUninit;
/home/jcq/.cargo/registry/src/mirrors.ustc.edu.cn-61ef6e0cd06fb9b8/crossbeam-epoch-0.9.2/src/sync/queue.rs:11:use core::mem::MaybeUninit;
/home/jcq/.cargo/registry/src/mirrors.ustc.edu.cn-61ef6e0cd06fb9b8/maybe-uninit-2.0.0/src/lib.rs:10:pub use core::mem::MaybeUninit;
#![feature(maybe_uninit)]
#![cfg_attr(not(feature = "std"), no_std)]

#[cfg(not(feature = "std"))]
#[macro_use]
extern crate alloc;

#[cfg(not(feature = "std"))]
use alloc::vec::Vec;

#[cfg(feature = "serde")]
extern crate serde;

extern crate maybe_uninit;
#[cfg(not(feature = "std"))]
mod std {
    pub use core::*;
}
use maybe_uninit::MaybeUninit;
rustup default nightly-2020-03-12
echo "nightly-2020-03-12" > rust-toolchain

github.global.ssl.fastly.Net 98.159.108.71
github.com 52.74.223.119
    #![feature(slice_patterns)]





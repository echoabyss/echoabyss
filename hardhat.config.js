
 require("@nomicfoundation/hardhat-toolbox");
 require("dotenv").config();

 const privateKey = process.env.PRIVATE_KEY || "0x0000000000000000000000000000000000000000000000000000000000000000"; // Default to a zero key if not set, but ensure it's set in .env for real deployments
 const bscMainnetRpcUrl = process.env.BSC_MAINNET_RPC_URL || "https://bsc-dataseed.binance.org/";
 const bscTestnetRpcUrl = process.env.BSC_TESTNET_RPC_URL || "https://data-seed-prebsc-1-s1.binance.org:8545/";
 const bscscanApiKey = process.env.BSCSCAN_API_KEY || "";

 /** @type import('hardhat/config').HardhatUserConfig */
 module.exports = {
   solidity: "0.8.28", // Ensure this matches your pragma version
   networks: {
     bscTestnet: {
       url: bscTestnetRpcUrl,
       chainId: 97,
       accounts: [privateKey],
       gasPrice: 20000000000, // 20 Gwei, adjust as needed
     },
     bscMainnet: {
       url: bscMainnetRpcUrl,
       chainId: 56,
       accounts: [privateKey],
       // gasPrice: 5000000000, // 5 Gwei, adjust based on current network conditions
     },
   },
   etherscan: { // Used for contract verification on BSCScan
     apiKey: bscscanApiKey,
   },
 };
 

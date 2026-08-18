// ========================================================
// TeleBirr Loyalty Points Module
// ========================================================

/**
 * Standard Earn Rule (Pure Function)
 * Calculates 1 point for every 10 ETB spent.
 * @param {number} amountInETB - Amount spent
 * @returns {number} Points earned
 */
export const standardEarnRule = (amountInETB) => Math.floor(amountInETB / 10);

/**
 * Holiday Double-Points Earn Rule (Pure Function)
 * Calculates 2 points for every 10 ETB spent (Double Points!).
 * @param {number} amountInETB - Amount spent
 * @returns {number} Points earned
 */
export const holidayEarnRule = (amountInETB) => Math.floor(amountInETB / 10) * 2;

/**
 * Factory Function creating a Loyalty Account with Private State (Closure).
 * @param {number} initialPoints - Starting points balance (defaults to 0)
 * @returns {Object} Public API exposing earn, redeem, and balance operations
 */
export function createLoyaltyAccount(initialPoints = 0) {
  // PRIVATE VARIABLE: Kept private inside this function's scope via Closure.
  // Cannot be directly read or modified from outside code (e.g., account.points -> undefined)
  let points = initialPoints;

  return {
    /**
     * Higher-Order Method to earn points.
     * Accepts the spent amount AND an "earn rule" callback function.
     * 
     * @param {number} amountInETB - Amount spent in ETB
     * @param {Function} earnRuleFn - Pure function calculating points earned
     * @returns {number} The newly earned points count
     */
    earn(amountInETB, earnRuleFn = standardEarnRule) {
      if (amountInETB <= 0) return 0;
      
      // Calculate points using the provided earn rule function
      const earned = earnRuleFn(amountInETB);
      points += earned; // Mutate internal private state
      return earned; // Pure return value (no side effects)
    },

    /**
     * Redeems points from the balance.
     * Prevents balance from dropping below zero.
     * 
     * @param {number} amountToRedeem - Points requested for redemption
     * @returns {boolean} True if redemption succeeded, false if insufficient points
     */
    redeem(amountToRedeem) {
      if (amountToRedeem <= 0 || amountToRedeem > points) {
        return false; // Refuse redemption if insufficient balance
      }
      
      points -= amountToRedeem; // Safely subtract points
      return true;
    },

    /**
     * Getter function returning current points balance.
     * @returns {number} Current points balance
     */
    balance() {
      return points;
    }
  };
}
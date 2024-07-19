export default class Building {
    constructor(sqft) {
        if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
            throw new Error('Class extending Building must override evacuationWarningMessage');
          }
        this._sqft = sqft;
    }

    get sqft() {
        return this._sqft;
    }

}

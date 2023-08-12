const axios = require('axios');
const { expect } = require('chai');

const baseUr = 'http://localhost:3000';

describe('Status and error tests', () => {
    it('should return OK status', async () => {
        const response = await axios.get(`${baseUr}/status`);
        expect(response.status).to.equal(200);
        expect(response.data.status).to.equal('ok');
    })
    it('should return 404 error', async () => {
        try {
            await axios.get(`${baseUr}/status/404`);
        } catch (error) {
            expect(error.response.status).to.equal(404);
        }
    })
})